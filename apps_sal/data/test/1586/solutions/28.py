n = int(input())
if n & 1:
    print(0)
else:
    ans = 0
    x = 10
    while n >= x:
        ans += n // x
        x *= 5
    print(ans)
