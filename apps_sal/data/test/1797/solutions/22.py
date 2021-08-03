n = int(input())
p = list(map(int, input().split()))
p = [i - 1 for i in p]
vis = [False for _ in range(n)]

sz = [0]

for i in range(n):
    j = i
    cnt = 0
    while not vis[j]:
        vis[j] = True
        cnt += 1
        j = p[j]
    if 0 < cnt:
        sz.append(cnt)

sz.sort()
print(sum(list(map(lambda x: x * x, sz))) + 2 * sz[-1] * sz[-2])
