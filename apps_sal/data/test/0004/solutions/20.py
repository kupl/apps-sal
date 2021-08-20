def test(x):
    return '7' in str(x)


x = int(input())
(h, m) = [int(i) for i in input().split()]
ans = 0
while not test(h) and (not test(m)):
    if m - x < 0:
        if h == 0:
            h = 23
        else:
            h -= 1
        m = m - x + 60
    else:
        m -= x
    ans += 1
print(ans)
