N, K = map(int, input().split())
total = K
for i in range(N-1):
    total *= (K-1)
print(total)
