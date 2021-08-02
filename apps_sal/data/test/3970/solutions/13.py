# coding=utf-8
n, k = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
a.sort()
s = []
d = {}
m = 0
for i in a:
    if i % k != 0:
        s.append(i)
        d[i] = 1
        m += 1
    elif (i // k) not in d:
        s.append(i)
        d[i] = 1
        m += 1
print(m)
