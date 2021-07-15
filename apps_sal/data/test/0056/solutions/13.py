n, t = map(int,input().split())
m = (n+1)*n//2
a = [0]*((n+1)*n//2)
next = [-1]*((n+1)*n//2)
now = 1
layer = 1
for i in range(m-n):
    next[i] = (now, now+1)
    if layer*(layer+1)//2 == i+1:
        layer += 1
        now = layer*(layer+1)//2-1
    now += 1
for i in range(t):
    a[0]+=1024
    for j in range(0, m):
        if a[j] > 1024:
            if next[j] == -1:
                a[j] = 1024
            else:
                a[next[j][0]] += (a[j]-1024)//2
                a[next[j][1]] += (a[j]-1024)//2
                a[j] = 1024
res = 0
for i in range(m):
    if a[i] >= 1024:
        res += 1
print(res)
