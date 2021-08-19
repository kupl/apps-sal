(a, b, k) = map(int, input().split())
a = a - k
if a < 0:
    b += a
    a = 0
    if b < 0:
        b = 0
print(str(a) + ' ' + str(b))
