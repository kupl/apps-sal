import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


def solve():
    n, k = nm()
    l = [1] * (k - 1) + [n - k + 1]
    if l[-1] > 0 and l[-1] % 2:
        print('YES')
        print(*l)
        return
    l = [2] * (k - 1) + [n - 2 * (k - 1)]
    if l[-1] > 0 and l[-1] % 2 == 0:
        print('YES')
        print(*l)
        return
    print('NO')
    return


T = ni()
for _ in range(T):
    solve()
