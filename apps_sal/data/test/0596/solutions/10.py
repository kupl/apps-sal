from datetime import date
d1 = date(*map(int, input().split(':')))
d2 = date(*map(int, input().split(':')))
print(abs(d2 - d1).days)
