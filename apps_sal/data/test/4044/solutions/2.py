a, b, x = list(map(int, input().split()))
if a > b:
    c = 0
else:
    c = 1
for i in range(x):
    print(c, end='')
    if i == x - 1:
        if c == 0:
            print("0" * (a - 1), end='')
            a = 0
        else:
            print("1" * (b - 1), end='')
            b = 0
    if c == 0:
        a -= 1
    else:
        b -= 1
    c ^= 1
print("1" * b, end='')
print("0" * a, end='')
