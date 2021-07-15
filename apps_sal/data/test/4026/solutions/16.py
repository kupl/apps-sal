from math import *
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    yes = 0
    for i in range(n):
        b = [list(map(int, input().split())), list(map(int, input().split()))]
        if b[0][1] == b[1][0]:
            yes = 1
    if m % 2 == 1:
        print('NO')
    elif yes == 0:
        print('NO')
    else:
        print('YES')


