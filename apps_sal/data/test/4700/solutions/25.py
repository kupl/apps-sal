import sys
(n, m) = map(int, sys.stdin.readline().split())
data = {}
h = [int(i) for i in sys.stdin.readline().split()]
for i in range(1, n + 1):
    data[i] = set()
for i in range(1, m + 1):
    (a, b) = map(int, sys.stdin.readline().split())
    data[a].add(b)
    data[b].add(a)
ans = 0
for i in data:
    if len(data[i]) == 0:
        ans += 1
    elif all((h[i - 1] > h[j - 1] for j in data[i])):
        ans += 1
print(ans)
