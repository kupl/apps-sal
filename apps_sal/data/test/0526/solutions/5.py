from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n, m = mi()

matrix = []

for i in range(n):
    matrix.append(lm())
done = 0
good = -1
for i in range(n):
    val = matrix[i][0]
    for j in range(m):
        if not matrix[i][j] == val:
            good = (i, j)
            done = 1
            break
    if done == 1:
        break
start = 0
if good == -1:
    for i in range(n):
        start = start ^ matrix[i][0]

    if start == 0:
        print('NIE')

    else:
        print("TAK")
        out = ['1'] * n
        print(*out)


else:
    answers = []
    for i in range(n):
        start = start ^ matrix[i][0]

    if not start == 0:
        print("TAK")
        out = ['1'] * n
        print(*out)

    else:

        extra = 0

        for i in range(n):
            if not i == good[0]:
                extra = extra ^ matrix[i][0]
                answers.append('1')
            else:
                extra = extra ^ matrix[i][good[1]]
                answers.append(str(good[1] + 1))

        print('TAK')
        print(*answers)
