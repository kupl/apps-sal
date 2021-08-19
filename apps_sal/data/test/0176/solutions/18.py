(k, a, b) = input().split(' ')
k = int(k)
a = int(a)
b = int(b)
if a == b and a % k == 0:
    print('1')
elif a * b > 0:
    a = abs(a)
    b = abs(b)
    if a > b:
        tmp = a
        a = b
        b = tmp
    print(b // k - (a - 1) // k)
elif a * b < 0:
    if a > 0:
        tmp = a
        a = b
        b = tmp
    print(b // k + abs(a) // k + 1)
else:
    a = abs(a)
    b = abs(b)
    if a != 0:
        tmp = a
        a = b
        b = tmp
    print(b // k + 1)
