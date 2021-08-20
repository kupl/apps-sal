n = int(input())
cl = list(map(int, input().split()))
m = int(input())
cp = list(map(int, input().split()))
cl = sorted(cl)
sm = 0
sl = [0]
for i in range(n):
    sm += cl[i]
    sl.append(sm)
res = []
sm = sum(cl)
for i in range(m):
    t = sm - cl[n - cp[i]]
    res.append(t)
for x in res:
    print(x)
