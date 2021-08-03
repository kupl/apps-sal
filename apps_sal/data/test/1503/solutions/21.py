n, m = list(map(int, input().split()))

graph = [0] * n
_next = [True] * n
_next[-1] = False


def read_array():
    return list([x - 1 for x in list(map(int, input().split()))])


first = read_array()


for i in range(n):
    graph[first[i]] = i

for _ in range(1, m):
    a = read_array()
    for i in range(n - 1):

        if graph[a[i]] + 1 != graph[a[i + 1]]:
            _next[graph[a[i]]] = False
    _next[graph[a[n - 1]]] = False

l = 0
ans = 0
for _ in range(n):
    l += 1
    if not _next[_]:
        ans += (l * (l + 1)) // 2
        l = 0

print(ans)
