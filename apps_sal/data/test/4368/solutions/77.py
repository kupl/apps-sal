N, K = map(int, input().split())
print(sum(N >= K ** i for i in range(99)))
