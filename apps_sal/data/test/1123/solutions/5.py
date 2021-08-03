N, K = map(int, input().split())
li = [0] * (K + 1)

out = 0
mod = 10**9 + 7

for i in range(K, 0, -1):
    li[i] = pow(K // i, N, mod)
    for j in range(i * 2, K + 1, i):
        li[i] -= li[j]
    out += li[i] * i
print(out % mod)
