
from collections import deque


def ri():

    return list(map(int, input().split()))


n = int(input())

v = [0] * n

c = [0] * n

p = [0] * n

adj = [set() for i in range(n)]

for i in range(n - 1):

    a, b = ri()

    a -= 1

    b -= 1

    adj[a].add(b)

    adj[b].add(a)

for s in range(n):

    if len(adj[s]) == 1:

        break

ans = 0

q = deque()

q.append(s)

v[s] = 1

c[s] = 1

p[s] = s

while q:

    n = q.popleft()

    cc = 1

    for a in adj[n]:

        if v[a] == 0:

            while cc in [c[n], c[p[n]]]:

                cc += 1

            c[a] = cc

            cc += 1

            ans = max(2 + len(adj[a]) - 1, ans)

            q.append(a)

            p[a] = n

            v[a] = 1

print(ans)

print(" ".join(map(str, c)))
