(x, n) = list(map(int, input().split()))
ppp = []
if n != 0:
    ppp = list(map(int, input().split()))
plus_x = x
minus_x = x
ans = 0
if x not in ppp:
    ans = x
else:
    while minus_x + 100 > x or plus_x + 100 > x:
        minus_x -= 1
        if minus_x not in ppp:
            ans = minus_x
            break
        plus_x += 1
        if plus_x not in ppp:
            ans = plus_x
            break
print(ans)
