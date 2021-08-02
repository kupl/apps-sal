from datetime import date
y1, m1, d1 = list(map(int, input().split(':')))
y2, m2, d2 = list(map(int, input().split(':')))

a = date(y1, m1, d1)
b = date(y2, m2, d2)
print(abs((b - a).days))
