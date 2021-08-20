(n, m) = list(map(int, input().split()))
t = 4 * 60 - m
o = 0
a = 5
otv = 0
while o + a <= t and otv < n:
    o += a
    a += 5
    otv += 1
print(otv)
