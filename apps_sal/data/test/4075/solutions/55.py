(n, m) = list(map(int, input().split(' ')))
k = []
s = []
for i in range(m):
    a = list(map(int, input().split(' ')))
    k.append(a[0])
    s.append(a[1:])
p = list(map(int, input().split(' ')))
ans = 0
for i in range(2 ** n):
    ri_cnt = 0
    for j in range(m):
        sw_cnt = 0
        for l in range(k[j]):
            if i >> s[j][l] - 1 & 1:
                sw_cnt += 1
        if sw_cnt % 2 == p[j]:
            ri_cnt += 1
    if ri_cnt == m:
        ans += 1
print(ans)
