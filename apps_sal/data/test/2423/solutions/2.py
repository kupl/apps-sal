N = int(input())
src = [tuple([int(x) - 1 for x in input().split()]) for i in range(N - 1)]
es = [[] for i in range(N)]
for (a, b) in src:
    es[a].append(b)
    es[b].append(a)
ans = 0
for e in es:
    if len(e) == 1:
        ans += 1
print(ans)
