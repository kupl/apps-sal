n = int(input())
p = list(map(int, input().split()))
ans = []
tmp = 1
for i in range(n - 1):
    if p[i] == tmp:
        for j in range(i, tmp - 1, -1):
            (p[j], p[j - 1]) = (p[j - 1], p[j])
            ans.append(j)
        tmp = i + 1
for j in range(n - 1, tmp - 1, -1):
    (p[j], p[j - 1]) = (p[j - 1], p[j])
    ans.append(j)
for (i, p) in enumerate(p, 1):
    if i != p:
        ans = -1
if ans == -1:
    print(ans)
else:
    print(*ans, sep='\n')
