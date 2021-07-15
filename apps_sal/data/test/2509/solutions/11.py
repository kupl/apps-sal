N, K = map(int, input().split())

cnt = 0

for i in range(K+1, N+1):
    cnt += (N // i)*(i - K)
    if N%i >= K: cnt += N%i - K + 1
if K == 0:cnt -= N
print(cnt)
