n, k = list(map(int, input().split()))
cnt, day = 0, 0
a = list(map(int, input().split()))
while k > 0:
    try:
        cnt += a[day]
    except IndexError:
        print(-1)
        return
    x = min(8, cnt)
    cnt -= x
    k -= x
    day += 1
print(day)


