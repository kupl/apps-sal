n, w, v, u = list(map(int, input().split()))
maxwait = 0.0
curr = 1
for i in range(n):
    x, y = list(map(int, input().split()))
    maxwait = max(maxwait, x / v - y / u)
    if(x / v < y / u):
        curr = 0
if(curr == 1):
    maxwait = 0
print(w / u + maxwait)
