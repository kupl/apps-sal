(n, m) = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    tmp = []
    cnt = [0] * n
    for j in range(n):
        if i >> j & 1:
            tmp.append(j + 1)
    for k in range(m):
        if len(set(tmp) & set(s[k])) % 2 != p[k]:
            break
    else:
        ans += 1
print(ans)
