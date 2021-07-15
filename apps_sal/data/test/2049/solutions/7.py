from sys import stdin

input = stdin.readline

[n, q] = [int(item) for item in input().split(' ')]
arr = [int(item) for item in input().split(' ')]
queries = [[int(item) for item in input().split(' ')] for i in range(q)]

b = [1]

for i in range(1, n):
    b.append((b[-1] + 1) if arr[i] <= arr[i - 1] else 1)

c = [1]
for i in reversed(list(range(n - 1))):
    c.append(c[-1] + 1 if arr[i] <= arr[i + 1] else 1)
c = [item for item in reversed(c)]

for query in queries:
    (x, y) = query
    x -= 1
    y -= 1
    print('Yes' if (x + c[x] > y) or (y - b[y] < x) or (x + c[x] > y - b[y]) else 'No')
"""
5 1
1 3 3 2 2
1 4

5 1
1 2 2 1 1
1 4

5 1
2 2 1 1 2
1 5
"""

