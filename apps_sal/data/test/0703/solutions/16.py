(k, a, b, v) = list(map(int, input().split(' ')))
(c, i) = (1, 1)
while a - v > 0:
    a -= v
    if i < k and b > 0:
        i += 1
        b -= 1
    else:
        i = 1
        c += 1
print(c)
