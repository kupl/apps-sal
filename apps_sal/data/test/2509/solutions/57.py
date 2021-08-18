N, K = map(int, input().split())

cnt = 0
if K == 0:
    cnt = N * N
else:
    for b in range(1, N + 1):
        p = N // b
        q = N % b
        cnt += p * max(0, b - K)
        cnt += max(0, q - K + 1)


print(cnt)
