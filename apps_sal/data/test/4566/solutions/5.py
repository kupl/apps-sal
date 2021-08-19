(n, m) = list(map(int, input().split()))
AB = [[] for _ in range(n)]
for i in range(m):
    (a, b) = [int(x) - 1 for x in input().split()]
    AB[a].append(b)
    AB[b].append(a)
for i in range(n):
    print(len(AB[i]))
