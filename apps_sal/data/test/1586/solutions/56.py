n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = 0
    n5 = 10
    while n >= n5:
        ans += n // n5
        n5 *= 5
    print(ans)
