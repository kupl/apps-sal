import bisect
import time
li = []
si = []

st = ""
for i in range(23000):
    st = st + str(i + 1)


def findn(b):
    return st[b - 1]


def calc(a):
    if 1 <= a <= 9:
        return a
    elif 10 <= a <= 99:
        return 2 * (a - 9) + 9
    elif 100 <= a <= 999:
        return 3 * (a - 99) + 189
    elif 1000 <= a <= 9999:
        return 4 * (a - 999) + 2889
    else:
        return 5 * (a - 9999) + 38889


for i in range(22000):
    li.append(calc(i + 1))

summ = 0
for j in li:
    summ += j
    si.append(summ)

_1 = time.time_ns()
q = int(input())
for i in range(q):
    x = int(input())
    zz = bisect.bisect(si, x - 1)
    if x == 1:
        print("1")
    else:
        print(st[x - si[zz - 1] - 1])
_2 = time.time_ns()
