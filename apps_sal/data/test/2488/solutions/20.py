import math
n, d, a = list(map(int,input().split()))
e = [[] for i in range(n)]
for i in range(n):
    x, h = list(map(int,input().split()))
    e[i] = [x,h]
num = 0

e.sort()
sd = [0 for i in range(n)]
l = [i for i in range(n)]
for i in range(n):
    for j in range(l[i-1],i):
        if e[i][0]-e[j][0] <= 2*d:
            l[i] = j
            break

for i in range(n):
    res = e[i][1] - sd[i-1] + sd[l[i]-1]
    if res < 0:
        sd[i] = sd[i-1]
    else:
        k = math.ceil(res/a)
        sd[i] = sd[i-1]+k*a
        num += k

print(num)

