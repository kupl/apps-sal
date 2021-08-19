n = int(input())
data1 = [list(map(int, input().split())) for _ in range(n)]
data2 = [list(map(int, input().split())) for _ in range(n)]
ans = []
trans = -1
for i in range(2 ** 10):
    S = [0] * n
    l = 0
    for j in range(10):
        for k in range(n):
            S[k] += data1[k][j] * (i >> j & 1)
    for j in range(n):
        l += data2[j][S[j]]
    ans.append(l)
    if not i:
        trans = l
ans.sort()
print(ans[-1] if ans[-1] != trans else ans[-2])
