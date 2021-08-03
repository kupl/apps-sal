from itertools import *
n = int(input())
l = list(map(int, input().split()))
for j in range(0, 2):
    m = {}
    l = [0] + list(reversed(l))
    for i in range(len(l)):
        m[l[i]] = i
    ac = list(accumulate(l))
    s = ac[-1]
    for i in range(0, len(ac) - 1):
        if ac[i] == s / 2 or (s / 2 - ac[i] in m.keys() and m[s / 2 - ac[i]] > i):
            print('YES')
            quit()
print('NO')
