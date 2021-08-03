from datetime import date
from datetime import timedelta

a = input()
a = [int(x) for x in a.split(":")]
b = input()
b = [int(x) for x in b.split(":")]

x = date(a[0], a[1], a[2])
y = date(b[0], b[1], b[2])

if x > y:
    x, y = y, x

ans = 0
while x != y:
    x = x + timedelta(days=1)
    ans += 1
print(ans)
