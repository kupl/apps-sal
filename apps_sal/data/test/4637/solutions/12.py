import sys

readline = sys.stdin.readline
readall = sys.stdin.read
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


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
