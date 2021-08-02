from datetime import date

d = [0] * 2

for i in range(0, 2):
    a = list(map(int, input().split(':')))
    d[i] = date(a[0], a[1], a[2])

r = (d[0] - d[1]).days

print(r if r >= 0 else -r)
