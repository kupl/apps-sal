n = int(input())
x = list(map(int,input().split()))
y = x.copy()
y.sort()
z = set(x)
t1 = y[n//2-1]
t2 = y[n//2]
idx = dict([])
idx[y[0]] = 0
l = y[0]
cnt = 0
for i in y:
    if i == l:
        cnt += 1
        continue
    else:
        idx[i] = cnt
        l = i
        cnt += 1

for i in x:
    t = idx[i]
    if t<n//2:
        print(t2)
    else:
        print(t1)
