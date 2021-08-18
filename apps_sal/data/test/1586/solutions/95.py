n = int(input())
if n % 2 == 1:
    print((0))
else:
    ans = 0
    num = 5
    n = n // 2
    while num <= n:
        ans += n // num
        num = num * 5
    print(ans)
