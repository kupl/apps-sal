n = int(input())
if n % 2 != 0:
    print(0)
else:
    ans = 0
    tmp = 10
    while tmp <= n:
        ans += n // tmp
        tmp *= 5
    print(int(ans))
