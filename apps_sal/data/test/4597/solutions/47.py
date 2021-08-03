n = int(input())
mod = 1000000007
res = 1
for i in range(1, n + 1):
    res = res * i % mod

print(res)
