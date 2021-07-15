n, C = map(int, input().split())
stc = [list(map(int, input().split())) for i in range(n)]
m = 0
for i in stc:
    m = max(m, i[1])
lis = [[0] * C for i in range(m + 1)]
for i in stc:
    for j in range(i[0], i[1] + 1):
        lis[j][i[2] - 1] = 1
ans = 0
for i in lis:
    ans = max(ans, sum(i))
print(ans)
