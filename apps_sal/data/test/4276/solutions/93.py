N,T = map(int, input().split())
tl = []
for i in range(N):
    c,t = map(int, input().split())
    if t <= T:
        tl.append(c)
if len(tl) == 0:
    print('TLE')
else:
    print(min(tl))
