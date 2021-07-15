[N, M] = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]
dic = {}
for i in range(M):
    [a, b] = [int(i) for i in input().split()]
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]
    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]

ans = 0
for i in range(1, N+1):
    s = H[i-1]
    t = 0
    if i in dic:
        for j in range(len(dic[i])):
            if s <= H[dic[i][j]-1]:
                t += 1
                break
        if t == 0:
            ans += 1
    else:
        ans += 1

print(ans)
