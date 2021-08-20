import math


def r():
    return int(input())


def ra():
    return [*list(map(int, input().split()))]


def s(a):
    if a <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True


n = r()
a = ra()
o = [i for i in a if i == 1]
o = len(o)
t = len(a) - o
b = 0
an = []
while o != 0 and t != 0:
    if s(b + 1):
        an += [1]
        o -= 1
        b += 1
    else:
        an += [2]
        t -= 1
        b += 2
if o == 0:
    a = [2] * t
else:
    a = [1] * o
an += a
print(*an)
