mod = 998244353
n = int(input())
p = list(map(int, input().split()))
i100 = pow(100, mod - 2, mod)
p = [i * i100 % mod for i in p]

top = 1
for i in range(n - 2, -1, -1):
    top *= p[i]
    top += 1
    top %= mod

bot = 1
for i in range(n):
    bot *= p[i]
    bot %= mod

ans = top * pow(bot, mod - 2, mod) % mod
print(ans)
