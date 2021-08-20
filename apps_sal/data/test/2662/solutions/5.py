import sys
input = sys.stdin.readline


def bisect_right_reverse(L, target):
    ok = len(L)
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if L[mid] < target:
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
A = [int(input()) for _ in range(N)]
dp = [-1]
for i in range(N):
    k = bisect_right_reverse(dp, A[i])
    if k == len(dp):
        dp.append(A[i])
    else:
        dp[k] = A[i]
print(len(dp))
