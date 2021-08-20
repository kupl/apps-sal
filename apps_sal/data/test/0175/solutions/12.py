(a, b) = map(int, input().split())
while a and b:
    c = 0
    while a > 0 and b > 0 and (a >= 2 * b):
        a -= 2 * b * (a // (2 * b))
        c = 1
    while a > 0 and b > 0 and (b >= 2 * a):
        b -= 2 * a * (b // (2 * a))
        c = 1
    if c == 0:
        break
print(a, b)
