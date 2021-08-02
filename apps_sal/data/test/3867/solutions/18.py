from queue import Queue
n = int(input())
g = [set() for i in range(n + 1)]
for i in range(n - 1):
    u, v = list(map(int, input().split()))
    g[u].add(v)
    g[v].add(u)

a = list(map(int, input().split()))
if a[0] != 1:
    print("No")
    return
ptr = 0
i = 1

while i < n:
    par = a[ptr]
    while len(g[par]) != 0:
        if a[i] not in g[par]:
            print("No")
            return
        else:
            g[par].remove(a[i])
            g[a[i]].remove(par)
        i += 1
    ptr += 1
print("Yes")
