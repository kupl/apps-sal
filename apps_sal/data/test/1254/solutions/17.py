n, m = map(int, input().split())
vec = [[] for j in range(100007)]
vt = [[] for j in range(100007)]
cv = []
ck = [0 for i in range(100007)]

for i in range(n):
    s, r = map(int, input().split())
    vec[s].append(r)
    if (ck[s] == 0):
        cv.append(s)
        ck[s] = 1

for i in cv:
    vec[i].sort(reverse=True)
    psum = 0
    for j in range(len(vec[i])):
        psum = psum + vec[i][j]
        vt[j].append(psum)

for i in range(100007):
    if len(vt[i]) == 0:
        break
    vt[i].sort(reverse=True)

ans = 0
for i in range(100007):
    if len(vt[i]) == 0:
        break
    tmp = 0
    for j in range(len(vt[i])):
        if (i + 1) * (j + 1) > n:
            break
        if vt[i][j] <= 0:
            break
        tmp = tmp + vt[i][j]
    ans = max(ans, tmp)

print(ans)
