n, m = map(int, input().split())
vec = [[] for j in range(m)]
vt = [[] for j in range(n)]

for i in range(n):
    s, r = map(int, input().split())
    vec[s - 1].append(r)

for i in range(m):
    vec[i].sort(reverse=True)
    psum = 0
    for j in range(len(vec[i])):
        psum += vec[i][j]
        vt[j].append(psum)

ans = 0
for i in range(n):
    tmp = 0
    for j in range(len(vt[i])):
        if vt[i][j] > 0:
            tmp += vt[i][j]
    ans = max(ans, tmp)

print (ans)
