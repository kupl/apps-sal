from math import log
n = int(input())
for i in range(n):
    for j in range(n):
        print('W' if (i + j) % 2 else 'B', end='')
    print()
