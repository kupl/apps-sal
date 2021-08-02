a, b, x = map(int, input().split())

if a > b:
    print(0, end='')
    prev = 0
    a -= 1
else:
    print(1, end='')
    prev = 1
    b -= 1

for i in range(x - 1):
    if prev == 0:
        print(1, end='')
        prev = 1
        b -= 1
    else:
        print(0, end='')
        prev = 0
        a -= 1

if prev == 0:
    for i in range(a):
        print(0, end='')

    for i in range(b):
        print(1, end='')

else:
    for i in range(b):
        print(1, end='')

    for i in range(a):
        print(0, end='')
