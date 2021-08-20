(N, M) = list(map(int, input().split()))
swiches = []
for _ in range(M):
    swiches.append(list(map(int, input().split()))[1:])
p = list(map(int, input().split()))
temp = '0' + str(N) + 'b'
case = []
for i in range(2 ** N):
    case.append(format(i, temp))
for a in range(len(swiches)):
    for b in range(len(swiches[a])):
        swiches[a][b] -= 1
ans = 0
for x in case:
    flag = 0
    for i in range(M):
        temp = 0
        for j in swiches[i]:
            temp += int(x[j])
        if temp % 2 == p[i]:
            flag += 1
    if flag == M:
        ans += 1
print(ans)
