#!/usr/bin/env python

# input
n = int(input())
a = [0 for _ in range(n)]
x = [[] for _ in range(n)]
y = [[] for _ in range(n)]
for i in range(n):
    a[i] = int(input())
    for _ in range(a[i]):
        x_, y_ = list(map(int, input().split()))
        x_ -= 1
        x[i].append(x_)
        y[i].append(y_)

# calc
# Full search
max_honest = 0
for i in range(2**n):
    s = []
    tmp = i
    for _ in range(n):
        s.append(tmp % 2)
        tmp //= 2
    s = list(reversed(s))
    honest = sum(s)

    ok = True
    for j in range(n):
        for k in range(a[j]):
            if s[j] == 1 and s[x[j][k]] != y[j][k]:
                # print('######')
                #print('x[{}][{}] = {}'.format(j, k, x[j][k]))
                #print('y[{}][{}] = {}'.format(j, k, y[j][k]))
                #print('s[x[{}][{}]] = {}'.format(j, k, s[x[j][k]]))
                ok = False
                break
        if not ok:
            break

    if ok:
        if max_honest <= honest:
            max_honest = honest

print(max_honest)
