n = int(input())
a = list(input().split())

ans = 0
for x in a:
    num = ''
    for y in x:
        num += y+y
    num = int(num)
    ans += num
    ans %= 998244353

ans *= n
ans %= 998244353
print(ans)

