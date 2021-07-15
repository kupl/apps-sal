import itertools
n = int(input())
t1 = [[] for i in range(n)]
t2 = [[] for i in range(n)]
t3 = [[] for i in range(n)]
t4 = [[] for i in range(n)]

for i in range(n):
    a = list(input())
    t1[i] = a
w = input()

for i in range(n):
    a = list(input())
    t2[i] = a
w = input()

for i in range(n):
    a = list(input())
    t3[i] = a
w = input()

for i in range(n):
    a = list(input())
    t4[i] = a

rec1, rec2 = [0, 0, 0, 0], [0, 0, 0, 0]
for i in range(n):
    if i % 2 == 0:
        p = 1
    else:
        p = 0
    for j in range(n):
        if int(t1[i][j]) != p:
            rec1[0] += 1
        else:
            rec2[0] += 1
        p ^= 1

for i in range(n):
    if i % 2 == 0:
        p = 1
    else:
        p = 0
    for j in range(n):
        if int(t2[i][j]) != p:
            rec1[1] += 1
        else:
            rec2[1] += 1
        p ^= 1

for i in range(n):
    if i % 2 == 0:
        p = 1
    else:
        p = 0
    for j in range(n):
        if int(t3[i][j]) != p:
            rec1[2] += 1
        else:
            rec2[2] += 1
        p ^= 1

for i in range(n):
    if i % 2 == 0:
        p = 1
    else:
        p = 0
    for j in range(n):
        if int(t4[i][j]) != p:
            rec1[3] += 1
        else:
            rec2[3] += 1
        p ^= 1

R = [0, 1, 2, 3]
num = float("inf")
for a, b, c, d in itertools.permutations(R, 4):
    num = min(num, rec1[a] + rec1[b] + rec2[c] + rec2[d])

print(num)
