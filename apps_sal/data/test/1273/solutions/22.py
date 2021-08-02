N = int(input())

ip = []
hen = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    ip.append([a, b])
    hen[a].append(b)

p = [-1] * N

for i in range(N):
    x = 0
    for j, h in enumerate(hen[i]):
        if p[i] == j:
            x += 1
        p[h] = j + x

print(max(p) + 1)
for i in range(N - 1):
    print(p[ip[i][1]] + 1)
