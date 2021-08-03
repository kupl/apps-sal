N, K = list(map(int, input().split()))
N %= K
print((min(N, K - N)))
