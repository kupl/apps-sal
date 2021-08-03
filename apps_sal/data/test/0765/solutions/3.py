t, s, q = list(map(int, input().split(' ')))
c = 1
while s < t:
    x = q * s - s
    s += x
    c += 1
print(c - 1)
