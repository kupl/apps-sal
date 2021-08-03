from datetime import date

s1 = list(map(int, input().split(':')))
s2 = list(map(int, input().split(':')))
a = date(s1[0], s1[1], s1[2])
b = date(s2[0], s2[1], s2[2])
x = abs((a - b).days)
print(x)
