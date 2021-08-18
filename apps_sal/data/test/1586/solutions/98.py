n = int(input())

ans = 0
if n % 2 == 1:
    ans = 0
else:
    ans += n // 10
    n = n // 10
    while n > 1:
        ans += n // 5
        n = n // 5
print(ans)
