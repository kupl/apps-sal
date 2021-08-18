N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (N + 1)
for i in range(N):
    B[A[i]] += 1
B.sort(reverse=True)
cnt = 0
for i in range(K):
    cnt += B[i]
print(N - cnt)
