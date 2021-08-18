import collections
n, m = list(map(int, input().split()))
visited = [False] * n
ships = [set() for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    ships[a - 1].add(b - 1)
    ships[b - 1].add(a - 1)

for i in range(1, n - 1):
    if 0 in ships[i] and n - 1 in ships[i]:
        print('POSSIBLE')
        return
print('IMPOSSIBLE')
