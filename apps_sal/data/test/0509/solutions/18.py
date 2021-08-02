from itertools import combinations
n = int(input())
u = []
for i in range(n):
    u.append(int(input()))
s = sum(u)
ans = s
k = 0
for i in range(n // 2 + 1):
    a = combinations(u, i)
    for j in a:
        s1 = sum(j)
        if abs(s - s1 * 2) % 360 < ans:
            ans = abs(s - s1 * 2) % 360
if ans != 0:
    print('NO')
else:
    print('YES')
