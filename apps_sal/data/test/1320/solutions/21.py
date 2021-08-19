n = int(input())
maps = []
ans = 0
for i in range(n):
    maps.append(input())
    ans += (maps[-1].count('C') - 1) * maps[-1].count('C') // 2
for i in range(n):
    cnt = 0
    for j in range(n):
        if maps[j][i] == 'C':
            cnt += 1
    ans += (cnt - 1) * cnt // 2
print(ans)
