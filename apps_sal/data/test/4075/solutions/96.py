(N, M) = list(map(int, input().split()))
li = []
ans = 0
for i in range(M):
    s = list(map(int, input().split()))
    li.append(s)
p = list(map(int, input().split()))
for j in range(2 ** N):
    j = bin(j)
    j = str(j)
    j = j[2:]
    while len(j) != N:
        j = '0' + j
    flash = 0
    for k in range(M):
        temp = 0
        for l in range(li[k][0]):
            if j[li[k][l + 1] - 1] == '1':
                temp += 1
        if temp % 2 == p[k]:
            flash += 1
    if flash == M:
        ans += 1
print(ans)
