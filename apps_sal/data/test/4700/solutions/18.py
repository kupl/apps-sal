N, M = map(int, input().split())
H = list(map(int, input().split()))
road = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    road[a - 1].append(b)
    road[b - 1].append(a)
c = 0
for i in range(N):
    T = True
    for j in road[i]:
        if H[i] <= H[j - 1]:
            T = False
    if T:
        c += 1
print(c)
