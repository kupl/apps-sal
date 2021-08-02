import sys
from functools import cmp_to_key


def val(s):
    cnt = 0
    ret = 0
    for c in s:
        if c == "s":
            cnt += 1
        else:
            ret += cnt
    return ret


def cmp(a, b):
    v1 = val(a + b)
    v2 = val(b + a)
    if v1 < v2:
        return 1
    elif v1 > v2:
        return -1
    return 0


ans = ""
s = []

n = int(input())

for i in range(0, n):
    t = input()
    s.append(t);

s = sorted(s, key=cmp_to_key(cmp))

ans = "".join(s)

print(val(ans))
