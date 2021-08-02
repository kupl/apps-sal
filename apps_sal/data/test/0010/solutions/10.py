n = int(input())
s = 2
o = 0
if n % 7 == 0:
    s = 0
if n % 7 == 1:
    s = 1
if n % 7 == 6:
    o = 1
print((n // 7) * 2 + o, (n // 7) * 2 + s)
