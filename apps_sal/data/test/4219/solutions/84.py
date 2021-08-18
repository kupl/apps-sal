"""
Created on Sun Sep 13 02:01:40 2020

@author: liang
"""

N = int(input())
A = list()
T = [list() for i in range(N)]

for i in range(N):
    a = int(input())
    A.append(a)
    for a in range(a):
        x, y = list(map(int, input().split()))
        x -= 1
        T[i].append((x, y))
ans = 0
for i in range(2**N):
    persons = list()
    for j in range(N):
        if i >> j & 1 == 1:
            persons.append(j)
    d = [False] * N
    for p in persons:
        d[p] = True

    judged = [False] * N
    for num in range(N):
        f = False
        if d[num]:
            for t in T[num]:
                x, y = t[0], t[1]
                if y == 1 and d[x] != True:
                    f = True
                    break
                if y == 0 and d[x] != False:
                    f = True
                    break
        if f:
            break
    else:
        ans = max(ans, len(persons))
print(ans)
