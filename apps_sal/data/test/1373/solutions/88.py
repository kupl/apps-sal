N, K = [int(x) for x in input().split()]

ans = 0
for k in range(K, N + 2):
    ans = (ans + k * (N - k + 1) + 1) % (10 ** 9 + 7)

print(ans)
