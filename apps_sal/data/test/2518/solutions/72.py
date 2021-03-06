import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = 10 ** 9
eps = 10 ** (-7)
(N, A, B) = list(map(int, readline().split()))
h = [int(readline()) for i in range(N)]
C = A - B
ng = 0
ok = INF


def judge(mid):
    ans = 0
    for hi in h:
        ans += max(0, (hi - mid * B + C - 1) // C)
    if ans <= mid:
        return True
    return False


while ok - ng > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok)
