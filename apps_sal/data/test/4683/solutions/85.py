N = int(input())
num = list(map(int, input().split(' ')))
ans = 0
total = sum(num)
MOD = 10 ** 9 + 7
for a in num:
    total -= a
    ans += a * total
    ans %= MOD
ans %= MOD
print(ans)
