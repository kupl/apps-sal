(N, K) = map(int, input().split())
keta = 1
while N >= K:
    keta += 1
    N = N / K
print(keta)
