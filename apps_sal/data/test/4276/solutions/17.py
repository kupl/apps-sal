
n, t = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]

costs = []
for i in range(n):
    if l[i][1] <= t:
        costs.append(l[i][0])

if len(costs) == 0:
    print("TLE")
else:
    print((min(costs)))
