list = [0, 0, 0]
a, b = map(int, input().split())
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        list[0] += 1
    elif abs(a - i) == abs(b - i):
        list[1] += 1
    else:
        list[2] += 1
for i in range(3):
    print(list[i], end=' ')
