t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    while n > 1:
        h = 1
        now = 2
        while n >= now + 2 * (h + 1) + h:
            now += (h + 1) * 2 + h
            h += 1
        n -= now
        cnt += 1
    print(cnt)
