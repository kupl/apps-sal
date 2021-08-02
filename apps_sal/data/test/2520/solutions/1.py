from collections import deque
N, M, K = map(int, input().split())

flst = []
blst = []
glooplst = [i for i in range(N + 1)]
colorlst = [0] * (N + 1)
countlst = [0] * (N + 1)
anslst = [0] * (N + 1)
d = deque()

for i in range(N + 1):
    flst.append([])
    blst.append([])


for i in range(M):
    a, b = map(int, input().split())
    flst[a].append(b)
    flst[b].append(a)


for i in range(K):
    a, b = map(int, input().split())
    blst[a].append(b)
    blst[b].append(a)


for i in range(1, N + 1):
    if colorlst[i] == 0:
        d.append(i)
        colorlst[i] = 1
        countlst[i] += 1
        while d:
            now = d.popleft()
            for j in flst[now]:
                if colorlst[j] == 0:
                    d.append(j)
                    colorlst[j] = 1
                    glooplst[j] = i
                    countlst[i] += 1

for i in range(1, N + 1):
    cnt = countlst[glooplst[i]] - len(flst[i]) - 1
    for j in blst[i]:
        if glooplst[i] == glooplst[j]:
            cnt -= 1

    print(cnt, end=' ')

print()
