n = int(input())
p = list(map(int, input().split()))

f = [0]
for i in range(1, n + 1):
    f.append(f[i - 1] ^ i)

res = 0
for i in range(1, n + 1):
    res = res ^ p[i - 1] ^ (f[i - 1] * ((n // i) % 2)) ^ f[n % i]

print(res)
