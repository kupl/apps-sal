N, M = list(map(int, input().split()))
k = []
s = []
for i in range(M):
    a = list(map(int, input().split()))
    k.append(a[0])
    s.append(a[1:])
p = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
    ri_count = 0
    for j in range(M):
        sw_count = 0
        for l in range(k[j]):
            if i>>(s[j][l]-1) & 1:
                sw_count += 1
        if sw_count%2 == p[j]:
            ri_count += 1
    if ri_count == M:
        ans += 1
print(ans)

