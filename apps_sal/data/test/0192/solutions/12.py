(y, x) = list(map(int, input().split()))
a = x
b = x
c = x
k = 0
while a < y or b < y or c < y:
    if a < c + b - 1:
        a = c + b - 1
        k += 1
        if a >= y and b >= y and (c >= y):
            break
    if b < a + c - 1:
        b = a + c - 1
        k += 1
        if a >= y and b >= y and (c >= y):
            break
    if c < a + b - 1:
        c = a + b - 1
        k += 1
        if a >= y and b >= y and (c >= y):
            break
print(k)
