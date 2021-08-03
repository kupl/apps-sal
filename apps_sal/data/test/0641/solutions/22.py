import datetime
cur = datetime.date(2016, 1, 1)
day = datetime.timedelta(days=1)

l = input().split()
hit = int(l[0])
assert l[2] in ["week", 'month']
month = l[2] == "month"

tot = 0
while cur.year == 2016:
    if month:
        if cur.day == hit:
            tot += 1
    else:
        if cur.isoweekday() == hit:
            tot += 1
    cur += day
print(tot)
