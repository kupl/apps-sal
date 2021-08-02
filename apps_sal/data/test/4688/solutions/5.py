N, K = map(int, input().split())

res = 1

for i in range(N):
    if i == 0:
        res *= K
    else:
        res *= (K - 1)

print(res)
