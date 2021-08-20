import bisect
(N, M, K) = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
A = [0]
for i in range(N):
    A.append(arr1[i] + A[-1])
B = [0]
for i in range(M):
    B.append(arr2[i] + B[-1])
ans = 0
for i in range(N + 1):
    if A[i] > K:
        break
    j = bisect.bisect_right(B, K - A[i]) - 1
    ans = max(ans, i + j)
print(ans)
