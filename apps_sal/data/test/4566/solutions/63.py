N, M = map(int, input().split())
AB = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    AB[a - 1].append(b - 1)
    AB[b - 1].append(a - 1)
for i in range(N):
    print(len(AB[i]))
