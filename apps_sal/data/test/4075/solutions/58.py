n, m = map(int, input().split())
bulbs = []
ans = 0
for i in range(m):
    c = tuple(map(int, input().split()))
    bulbs.append(c[1:])
p = list(map(int, input().split()))
for i in range(2 ** n):
    cnt = 0
    for j, bulbs_sub in enumerate(bulbs):
        switch_on = 0
        for l in bulbs_sub:
            if i >> (l - 1) & 1:
                switch_on += 1
        if switch_on % 2 == p[j]:
            cnt += 1
    if cnt == m:
        ans += 1
print(ans)
