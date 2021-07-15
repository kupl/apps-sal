__author__ = 'ruckus'

x, y = map(int, input().split())

a = []

for i in range(y):
    a.append(input())

for i in range(x):
        for k in range(2):
            for j in range(y):
                print(a[j][i], end='')
                print(a[j][i], end='')
            print()
