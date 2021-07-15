n, m = map(int, input().split())
v1 = list(map(int, input().split()))
v = [[w, i] for i, w in enumerate(v1)]
v.sort(reverse = True)
d = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].add(b)
    d[b].add(a)
ans = 0
for w, i in v:
    for j in d[i]:
        ans += v1[j]
        d[j].discard(i)
        
print(ans)
