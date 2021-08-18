__author__ = 'RaldenProg'
from pprint import pprint
n, k = [_ for _ in map(int, input().split())]
top = ['.', 'P', '-', 'x']
top1 = ['S', '-', 'p', '.']
pas = ['P', 'x', 'S']
y = []
for i in range(n):
    x = ['-']
    x.extend(list(input()))
    x.append('-')
    y.append(x)

chet = 0

for i in range(n):
    for j in range(len(y[i])):
        if y[i][j] == '.':
            if y[i][j - 1] in top and y[i][j + 1] in top and chet != k:
                y[i][j] = 'x'
                chet += 1
while chet != k:
    flag = 0
    for i in range(n):
        for j in range(len(y[i])):
            if y[i][j] == '.':
                if y[i][j - 1] in top1 and y[i][j + 1] in top and chet != k:
                    y[i][j] = 'x'
                    chet += 1
                    flag = 1

                if y[i][j - 1] in top and y[i][j + 1] in top1 and chet != k:
                    y[i][j] = 'x'
                    chet += 1
                    flag = 1

    if flag == 0 and chet != k:
        for i in range(n):
            for j in range(len(y[i])):
                if y[i][j] == '.' and chet != k:
                    y[i][j] = 'x'
                    chet += 1
                    flag = 1

kol = 0
for i in range(n):
    for j in range(len(y[i])):
        if y[i][j] == 'S':
            if y[i][j - 1] in pas:
                kol += 1
            if y[i][j + 1] in pas:
                kol += 1
print(kol)
for i in range(n):
    for j in range(1, len(y[i]) - 1):
        print(y[i][j], end='')
    print()
