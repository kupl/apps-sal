'''
Created on 2019. 9. 21.

@author: kkhh88
'''
'''
a, b = map(int,input().split(' '))

t = 0

for i in range(a, b+1):
    x = [0] * 10
    n = i
    while n:
        x[n%10] = x[n%10] + 1
        n = n // 10
    n = 0
    for n in range(10):
        if x[n] > 1:
            break
    
    if n == 9 and x[n] < 2:
        print (i)
        t = 1
        break
    
if t == 0:
    print (-1)
'''

h, w = list(map(int,input().split(' ')))
r = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))

cnt = 0
x = [[-1 for _ in range(w)] for _ in range(h)]
for i in range(w):
    for j in range(c[i]):
        if x[j][i] == 1 or x[j][i] == -1:
            x[j][i] = 1
        else:
            cnt = -1
            break
    if cnt < 0:
        break
    if c[i] < h:
        if x[c[i]][i] == 0 or x[c[i]][i] == -1:
            x[c[i]][i] = 0
        else:
            cnt = -1
            break

for i in range(h):
    for j in range(r[i]):
        if x[i][j] == 1 or x[i][j] == -1:
            x[i][j] = 1
        else:
            cnt = -1
            break
    if cnt < 0:
        break
    if r[i] < w:
        if x[i][r[i]] == 0 or x[i][r[i]] == -1:
            x[i][r[i]] = 0 
        else:
            cnt = -1
            break

if cnt < 0:
    print(0)
else:
    for i in range(w):
        for j in range(h):
            if x[j][i] == -1:
                cnt = cnt + 1
    print((1<<cnt) % 1000000007)

