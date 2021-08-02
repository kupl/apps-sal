N, T = map(int, input().split())
ls = []
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ls.append(c)
if len(ls) == 0:
    print("TLE")
else:
    print(min(ls))
