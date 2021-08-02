def simulate(init, n):
    a = [0, 0, 0]
    a[init] = 1
    n %= 6
    for i in range(1, n + 1):
        if i % 2 == 1:
            a[0], a[1] = a[1], a[0]
        else:
            a[1], a[2] = a[2], a[1]
    for i in range(3):
        if a[i] == 1:
            return i


n = int(input())
x = int(input())
for i in range(3):
    if simulate(i, n) == x:
        print(i)
        break
