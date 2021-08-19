x = int(input())
(h, m) = map(int, input().split())
ans = 0
while h % 10 != 7 and m % 10 != 7:
    if m - x >= 0:
        m -= x
    else:
        temp = x - m
        m = 60 - temp
        if h - 1 >= 0:
            h -= 1
        else:
            h = 23
    ans += 1
print(ans)
