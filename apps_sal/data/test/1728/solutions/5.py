n = int(input())
p = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
res = 1
mp = {i: [] for i in range(1, n + 1)}
for i in range(1, len(p)):
    mp[p[i]].append(i + 1)
col = {i: 0 for i in range(1, n + 1)}
q = [1]
while q != []:
    cur = q.pop(0)
    for i in mp[cur]:
        q.append(i)
    if cur == 1:
        col[cur] = c[cur]
    else:
        col[cur] = col[p[cur - 1]]
        if col[cur] != c[cur]:
            col[cur] = c[cur]
            res += 1
print(res)
