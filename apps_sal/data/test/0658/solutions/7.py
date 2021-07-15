n, w, v, u = map(int, input().split())
maxwait = 0
curr = True
for i in range(n):
    x, y = map(int, input().split())
    maxwait = max(maxwait, x / v - y / u)
    if x / v < y / u:
        curr = False
if curr:
    maxwait = 0
print(w / u + maxwait)
