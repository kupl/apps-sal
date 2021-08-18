import sys
import math
import os.path

FILE_INPUT = "c.in"
DEBUG = os.path.isfile(FILE_INPUT)
if DEBUG:
    sys.stdin = open(FILE_INPUT)


def ni():
    return list(map(int, input().split(" ")))


def nia():
    return list(map(int, input().split()))


def log(x):
    if (DEBUG):
        print(x)


n, m, k = ni()

m1 = []
for _ in range(n):
    m1.append(list([x == '.' for x in input()]))

# log(m1)

count = 0

if (k == 1):
    count = 0
    print(sum(x.count(True) for x in m1))
    return

for i in range(n):
    j = 0
    while (j < m):
        cd = 0
        while (j < m) and (not m1[i][j]):
            j += 1
        while (j < m) and (m1[i][j]):
            j += 1
            cd += 1
        if (k <= cd):
            count += cd - k + 1
            # log(f"i = {i}, {j-cd} -> {j}")

# log(f"count = {count}")

for j in range(m):
    i = 0
    while (i < n):
        cd = 0
        while (i < n) and (not m1[i][j]):
            i += 1

        while (i < n) and (m1[i][j]):
            i += 1
            cd += 1

        if (k <= cd):
            count += cd - k + 1
            # log(f"j = {j}, {i-cd} -> {i}")
print(count)
