xh = []
n, d, a = list(map(int, input().split()))
for _ in range(n):
    x, h = list(map(int, input().split()))
    xh.append([x, h])
xh.sort()
ans = 0
cnt = [0] * n
j = 0
limit = []
for i in range(n):
    while xh[j][0] - xh[i][0] <= 2 * d:
        j += 1
        if j == n:
            break
    j -= 1
    limit.append(j)
num = [0] * (n + 1)
cnt = 0
for i in range(n):
    xh[i][1] -= (ans - cnt) * a
    damage_cnt = max(0, (xh[i][1] - 1) // a + 1)
    ans += damage_cnt
    num[limit[i]] += damage_cnt
    cnt += num[i]
print(ans)
