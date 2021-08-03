n = int(input())
if n % 2 != 0:
    print(0)
else:
    ans = 0
    t = 10
    while n >= t:
        ans += n // t
        t *= 5
    print(ans)
