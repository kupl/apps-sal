n = int(input())
a = n & 1
b = n >> 1 & 1
c = n >> 2 & 1
d = n >> 3 & 1

d = 1 - d
if d:
    c = 1 - c
if c and d:
    b = 1 - b
if b and c and d:
    a = 1 - a
ans = d << 3 | c << 2 | b << 1 | a
print(ans)
