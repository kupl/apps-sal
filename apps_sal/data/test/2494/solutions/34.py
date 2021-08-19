from collections import deque


def bfs01(K, adjlist):
    reached = [False] * K
    d = deque()
    d.append((1, 0))
    reached[1] = True
    while True:
        cur = d.popleft()
        reached[cur[0]] = True
        if cur[0] == 0:
            return cur[1]
        for (j, w) in adjlist[cur[0]]:
            if w == 0:
                if not reached[j]:
                    d.appendleft((j, cur[1]))
            elif w == 1:
                if not reached[j]:
                    d.append((j, cur[1] + 1))


K = int(input())
adjlist = [[] for _ in range(K)]
for i in range(K):
    to1 = (i + 1) % K
    to2 = 10 * i % K
    if to1 == to2:
        adjlist[i] = [(to2, 0)]
    else:
        adjlist[i] = [(to1, 1), (to2, 0)]
print(bfs01(K, adjlist) + 1)
