# :)
a = int(input())
b = int(input())
d = abs(a - b)
s = (1 + d // 2) * (d // 2)
if d % 2 == 1:
    s += d // 2 + 1
print(s)
