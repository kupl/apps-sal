t = int(input())
for _ in range(t):
    (n, x) = map(int, input().split())
    adj = [[] for i in range(n + 1)]
    for i in range(n - 1):
        (u, v) = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    if n <= 2:
        print('Ayush')
    elif len(adj[x]) <= 1:
        print('Ayush')
    elif n & 1:
        print('Ashish')
    else:
        print('Ayush')
