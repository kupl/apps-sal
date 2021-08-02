a, b = list(map(int, input().split()))
r = 0
while a > 0:
    if a >= b:
        r += b
        a = a - b + 1
    else:
        r += a
        a = 0
print(r)
