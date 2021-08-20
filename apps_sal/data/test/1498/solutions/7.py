import sys
input = sys.stdin.readline
(n, q) = list(map(int, input().split()))
servers = [0 for i in range(n)]
for i in range(q):
    (time, serv, leng) = list(map(int, input().split()))
    pos = []
    for j in range(n):
        if servers[j] <= time:
            pos.append(j)
    if len(pos) < serv:
        print(-1)
        continue
    pos = pos[:serv]
    for j in pos:
        servers[j] = time + leng
    print(sum(pos) + len(pos))
