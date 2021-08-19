import bisect
(N, M, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum1 = [0]
sum2 = [0]
for i in range(N):
    sum1.append(sum1[-1] + A[i])
for i in range(M):
    sum2.append(sum2[-1] + B[i])
ans = 0
for i in range(N + 1):
    if sum1[i] > K:
        break
    ans = max(ans, i + bisect.bisect_right(sum2, K - sum1[i]) - 1)
print(ans)
