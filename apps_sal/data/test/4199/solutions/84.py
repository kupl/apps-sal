N, K = map(int, input().split())
h = list(map(int, input().split()))
print(sum(h[i] >= K for i in range(N)))
