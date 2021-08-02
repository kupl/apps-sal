import sys
import math
import os.path

FILE_INPUT = "c.in"
DEBUG = os.path.isfile(FILE_INPUT)
if DEBUG:
    sys.stdin = open(FILE_INPUT)


def ni():
    return map(int, input().split(" "))


def nia():
    return list(map(int, input().split()))


def log(x):
    if (DEBUG):
        print(x)


n, = ni()
a = nia()
en = list(map(lambda x: x == '1', input()))

# log(n)
# log(a)
# log(en)

count = 1
i = 0
while (i < n - 1):
    if (en[i]):
        j = i
        b = [a[i]]
        while (j < n - 1 and en[j]):
            j += 1
            b.append(a[j])
        b.sort()
        # log(b)
        for j in b:
            if (j != count):
                print("NO")
                return
            else:
                count += 1
        i = j
    else:
        if (a[i] == count):
            count += 1
        else:
            print("NO")
            return
        i += 1


print("YES")
