from math import log2
for _ in range(int(input())):
    x = int(input())
    acc = 0
    for i in range(1, 60):
        acc += (2 ** i - 1) * 2 ** (i - 1)
        if acc > x:
            break
    print(i - 1)
