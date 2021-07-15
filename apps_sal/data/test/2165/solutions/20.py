import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, T = nm()
    a = nl()
    t = nl()
    if min(t) > T or max(t) < T:
        print(0)
        return
    g = [(t[i] - T, i) for i in range(n)]
    h = sum((t[i] - T)*a[i] for i in range(n))
    ans = sum(a)
    if h < 0:
        g.sort()
        for x, i in g:
            if h < x * a[i]:
                ans -= a[i]
                h -= x * a[i]
            else:
                if h and x != 0:
                    ans -= h / x
                break
    elif h > 0:
        g.sort(reverse=True)
        for x, i in g:
            if h > x * a[i]:
                ans -= a[i]
                h -= x * a[i]
            else:
                if h and x != 0:
                    ans -= h / x
                break
    print(ans)
    return

solve()

# T = ni()
# for _ in range(T):
#     solve()

