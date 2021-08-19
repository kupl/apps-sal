N = int(input())
count = [1 for _ in range(N + 2)]
count[-1] = 0
count[0] = 0
nextpoint = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (u, v) = list(map(int, input().split()))
    if u > v:
        nextpoint[v].append(u)
    else:
        nextpoint[u].append(v)
for k in range(N + 1):
    if len(nextpoint[k]) > 0:
        nextpoint[k].sort()
for k in range(1, N):
    for item in nextpoint[k]:
        count[item] -= 1
ans = 0
for k in range(1, N):
    count[k + 1] += count[k]
ans = sum(count)
before = ans
for k in range(1, N):
    before -= N - k + 1
    for item in nextpoint[k]:
        before += N + 1 - item
    ans += before
print(ans)
