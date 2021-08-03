n = int(input())
if n % 2 == 1:
    print((0))
    return
else:
    ans = 0
    u = 10
    while n // u >= 1:
        ans += n // u
        u = u * 5
    print((int(ans)))
