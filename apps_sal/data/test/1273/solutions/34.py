N = int(input())

ans = [0] * (N - 1)
to = [[] for i in range(N - 1)]
used = [0] * N

for i in range(N - 1):
    a, b = map(int, input().split())
    to[a - 1].append([b - 1, i])

for i in range(N - 1):
    unable = used[i]
    c = 1
    for j, id in to[i]:
        if c == unable:
            c += 1
        ans[id] = c
        used[j] = c
        c += 1

print(max(used))
for i in range(N - 1):
    print(ans[i])
