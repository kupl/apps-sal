n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

inf = 10**12
z = len(x)

if n == 1 and k == 1:
    print((0))
    return

for i in range(len(x)):
    if x[i] >= 0:
        z = i
        break

r = [inf] * (n - z)
l = [inf] * z

for i in range(n-z):
    r[i] = x[z+i]

for i in range(z):
    l[i] = abs(x[z-i-1])

# 左からすべて取る場合
tl = inf
if len(l) < k:
    tl = inf
else:
    tl = abs(l[k-1])

if z == n-1:
    print(tl)
    return

# 右からすべて取る場合
tr = inf
if len(r) < k:
    tr = inf
else:
    tr = abs(r[k-1])
    
# 両方から取る場合
# 右からi個取る
t_arr = []
for i in range(1,k):
    if i-1 >= len(r):
        pass
    else:
        if k-i-1 >= len(l):
            pass
        else:
            t1 = r[i-1]
            t2 = l[k-i-1]
            t_arr.append(t1*2 + t2*2 - max(t1,t2))
tc = inf
if len(t_arr) != 0:
    tc = min(t_arr)
else:
    tc = inf
print((min(tl,tr,tc)))

