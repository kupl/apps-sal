N,T = map(int, input().split())
l = []
for _ in range(N):
    c,t = map(int, input().split())
    if T >= t:
        l.append(c)
    else:
        l.append(1001)

print(min(l)) if min(l) < 1001 else print("TLE")
