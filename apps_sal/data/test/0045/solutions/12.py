(N, K) = map(int, input().split())
if K * (K + 1) // 2 > N:
    exit(print(-1))
ans = 1
for i in range(1, int(N ** 0.5) + 1):
    if N % i:
        continue
    if ans < i:
        if K * (K + 1) // 2 <= N // i:
            ans = i
    if ans < N // i:
        if K * (K + 1) // 2 <= i:
            ans = N // i
t = N // ans
for i in range(1, K + 1):
    print(i * ans if i < K else N - (K - 1) * K // 2 * ans, end=' \n'[i == K])
