n = int(input())
res = 1
mod = 10 ** 9 + 7
for i in range(1, n + 1):
    res = res * i % mod

print(res)
