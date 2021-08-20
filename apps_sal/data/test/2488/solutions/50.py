import math


def I():
    return list(map(int, input().split()))


(n, d, a) = I()
l = []
for _ in range(n):
    (x, y) = I()
    l.append([x, y])
l.sort()
j = 0
limit = []
for i in range(n):
    while l[j][0] - l[i][0] <= 2 * d:
        j += 1
        if j == n:
            break
    j -= 1
    limit.append(j)
ans = 0
num = [0] * (n + 1)
cnt = 0
for i in range(n):
    l[i][1] -= (ans - cnt) * a
    damage_cnt = max(0, (l[i][1] - 1) // a + 1)
    ans += damage_cnt
    num[limit[i]] += damage_cnt
    cnt += num[i]
print(ans)
