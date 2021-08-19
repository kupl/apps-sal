(N, K) = map(int, input().split())
print(sum(((N + 1 - n) * n + 1 for n in range(K, N + 2))) % (10 ** 9 + 7))
