from collections import deque
n = int(input())
ad_ls = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,w = list(map(int,input().split()))
    ad_ls[a-1].append([b-1,w])
    ad_ls[b-1].append([a-1,w])

cost_ls = [0] * n
done_ls = [0] * n
done_ls[0] = 1
q = deque()
q.append(0)

while q:
    now = q.pop()
    for new in ad_ls[now]:
        nex,cost = new[0],new[1]
        if not done_ls[nex]:
            cost_ls[nex] = cost + cost_ls[now]
            done_ls[nex] = 1
            q.append(nex)

color_ls = [0] * n
for i in range(n):
    color_ls[i] = cost_ls[i] % 2

for color in color_ls:
    print(color)


