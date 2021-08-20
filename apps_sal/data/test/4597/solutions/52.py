n = int(input())
mod = 10 ** 9 + 7
res = 1
for i in range(1, n + 1):
    res *= i
    res %= mod
print(res)
