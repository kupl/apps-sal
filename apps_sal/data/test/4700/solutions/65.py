n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
l = [1 for _ in range(n)]

for i in range(m):
    if h[a[i]-1] < h[b[i]-1]:
        l[a[i]-1] = 0
    elif h[a[i]-1] > h[b[i]-1]:
        l[b[i]-1] = 0
    else:
        l[b[i]-1] = 0
        l[a[i]-1] = 0

print((l.count(1))) 

