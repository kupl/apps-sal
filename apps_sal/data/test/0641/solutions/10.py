import datetime

ans = 0
x, *s = input().split()
cur = datetime.date(2016, 1, 1)
while cur.year != 2017:
    if s == ["of", "week"]:
        ans += (cur.isoweekday() == int(x))
    else:
        ans += (cur.day == int(x))
    cur += datetime.timedelta(1)
print(ans)
