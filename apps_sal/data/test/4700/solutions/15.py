(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
cor = [[] for i in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    cor[a].append(b)
    cor[b].append(a)
ans = 0
for i in range(n):
    max_h = l[i]
    cnt = 1
    co = list(set(cor[i]))
    for j in range(len(co)):
        if l[co[j]] >= max_h:
            cnt = 0
            break
    ans += cnt
print(ans)
