from heapq import *


def solve():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    a = []
    heapify(a)
    ans = []
    for i in range(X):
        for j in range(Y):
            if (i + 1) * (j + 1) > K:
                break
            for k in range(Z):
                if (i + 1) * (j + 1) * (k + 1) > K:
                    break
                heappush(a, -A[i] - B[j] - C[k])
    for _ in range(K):
        ans.append(-heappop(a))
    return ans


print(*solve(), sep='\n')
