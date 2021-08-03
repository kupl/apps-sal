from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge


def solve():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    Cake = []
    heapify(Cake)
    for i in range(X):
        for j in range(min(Y, K // (i + 1) + 1)):
            for k in range(min(Z, K // ((i + 1) * (j + 1)) + 1)):
                heappush(Cake, -A[i] - B[j] - C[k])
    ans = []
    for i in range(K):
        ans.append(abs(heappop(Cake)))
    return ans


print(*solve(), sep='\n')
