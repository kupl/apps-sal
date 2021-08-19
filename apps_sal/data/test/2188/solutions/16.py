import sys
import functools
commands = []


def less_int(x, y):
    return x[0] - y[0]


def more_int(x, y):
    return y[0] - x[0]


n = int(input())
ab = []
ba = []
for i in range(n):
    a_s = list(map(int, input().split(' ')))
    if a_s[0] > a_s[1]:
        ab.append((a_s[0], a_s[1], i + 1))
    else:
        ba.append((a_s[0], a_s[1], i + 1))
ab.sort(key=functools.cmp_to_key(less_int))
ba.sort(key=functools.cmp_to_key(more_int))
answ = ab
if len(ba) > len(ab):
    answ = ba
print(len(answ))
for (a, b, c) in answ:
    print(c, end=' ')
