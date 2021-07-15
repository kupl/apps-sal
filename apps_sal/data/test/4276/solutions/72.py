N,T = map(int, input().split())

cost = []

for i in range(N):
    c,t = map(int, input().split())
    if t <= T:
        cost.append(c) 

if len(cost) > 0:
    print(min(cost))
else:
    print("TLE")
