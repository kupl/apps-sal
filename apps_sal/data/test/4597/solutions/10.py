n = int(input())
mod = 7 + 10 ** 9
ans = 1
for i in range(1, n + 1):
    ans = ans * i % mod
print(ans)
