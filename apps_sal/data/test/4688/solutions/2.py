N, K = map(int, input().split())
P = K
for i in range(N - 1):
    P *= K - 1
print(P)
