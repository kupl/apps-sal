import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, k = nm()
    a = nl()
    b = nl()
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] >= b[i]:
            break
        a[i] = b[i]
    print(sum(a))
    return

# solve()

T = ni()
for _ in range(T):
    solve()

