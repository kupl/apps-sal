x = int(input())
(h, m) = map(int, input().split())
ans = 0
while 1:
    if '7' in str(h) + str(m):
        break
    ans += 1
    if m >= x:
        m -= x
    else:
        m = 60 - (x - m)
        h -= 1
        if h == -1:
            h = 23
print(ans)
