(c, d) = map(int, input().split())
(n, m) = map(int, input().split())
k = int(input())
tot = n * m
if k >= tot:
    print('0')
else:
    rem = tot - k
    x = n / c
    y = 1 / d
    ans = 0
    if x >= y:
        temp = rem // n
        bacha = rem % n
        if bacha * d <= c:
            ans = temp * c + bacha * d
        else:
            ans = (temp + 1) * c
    else:
        ans = rem * d
    print(ans)
