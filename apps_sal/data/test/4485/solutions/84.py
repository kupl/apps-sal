(N, M) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
dic = {}
for (a, b) in ab:
    if a in dic.keys():
        dic[a].append(b)
    else:
        dic[a] = [b]
check = False
for i in dic[1]:
    if i in dic.keys():
        for j in dic[i]:
            if j == N:
                check = True
print('POSSIBLE' if check else 'IMPOSSIBLE')
