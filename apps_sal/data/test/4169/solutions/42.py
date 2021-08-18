n, m = map(int, input().split())
dic = {}
for i in range(n):
    a, b = map(int, input().split())
    dic.setdefault(a, 0)
    dic[a] += b
nedan = sorted(dic)
ans = 0
for yen in nedan:
    if dic[yen] < m:
        ans += yen * dic[yen]
        m -= dic[yen]
    else:
        ans += yen * m
        break
print(ans)
