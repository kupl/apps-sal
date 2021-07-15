n, T = list(map(int, input().split()))

ct = [list(map(int, input().split())) for i in range(n)]

cost = []

for c, t in ct:
    if t <= T:
        cost.append(c)

if len(cost) == 0:
    print("TLE")
else:
    print(min(cost))
