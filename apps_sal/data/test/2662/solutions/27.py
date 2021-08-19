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
L = []
for i in range(N):
    k = bisect_right_reverse(L, A[i])
    if k == len(L):
        L.append(A[i])
    else:
        L[k] = A[i]
print(len(L))
