n = int(input())
ans = 0
if n % 2 == 1:
    ans = 0
else:
    tmp = 10
    while tmp <= n:
        ans += n // tmp
        tmp *= 5
print(ans)
