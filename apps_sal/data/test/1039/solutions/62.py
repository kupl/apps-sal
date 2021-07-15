from collections import namedtuple, deque
N = int(input())

connection = [[] for _ in range(N)]
branch = namedtuple('branch',['id', 'dist'])
for _ in range(N-1):
    a, b, c = list(map(int, input().split()))
    connection[a-1].append(branch(b-1, c))
    connection[b-1].append(branch(a-1, c))

dist = [0] * N #dist from root(K)
Q, K = list(map(int, input().split()))
#bfs
reserved = deque([K-1])
seen = {K-1}
while len(reserved) > 0:
    current = reserved.popleft()
    for next in connection[current]:
        if next.id in seen:
            continue
        seen.add(next.id)
        reserved.append(next.id)
        dist[next.id] = dist[current] + next.dist

#deal with query
Query = [list(map(int, input().split())) for _ in range(Q)]
for x,y in Query:
    print((dist[x-1] + dist[y-1]))



