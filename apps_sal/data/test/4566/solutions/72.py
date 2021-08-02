N, M = map(int, input().split())
list = []

for i in range(M):
    a, b = map(int, input().split())
    list.append(a)
    list.append(b)

for j in range(1, N + 1):
    print(list.count(j))
