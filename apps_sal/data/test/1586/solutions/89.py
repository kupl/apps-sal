n = int(input())
if n % 2 == 1:
    print(0)
else:
    x = 10
    ans = 0
    while n >= x:
        ans += n // x
        x *= 5
    print(ans)
