n = int(input())
v = list(map(int,input().split()))
m = int(input())
i = 0
u = list(v)
u.sort()
while i < n-1:
    v[i+1] += v[i];
    u[i+1] += u[i];
    i += 1
u, v = [0] + u, [0] + v
i = 0
while i < m:
    t, l, r = map(int,input().split())
    if t == 1: print(v[r] - v[l-1])
    else: print(u[r] - u[l-1])
    i += 1;
