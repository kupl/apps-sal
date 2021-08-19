n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = 0
    ans += n // 10
    n = n // 10
    while n // 5 > 0:
        ans += n // 5
        n = n // 5
    print(ans)
