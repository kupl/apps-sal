import sys


n, k = [int(i) for i in input().split()]
skill = [[int(i) % 10, int(i)] for i in input().split()]

skill.sort(reverse=True)
ans = 0
for i in range(n):
    ans += skill[i][1] // 10
for i in range(n):
    if skill[i][1] == 100:
        continue
    toup = 10 - skill[i][0]
    if k >= toup:
        k -= toup
        ans += 1
        skill[i][1] += toup


maxadd = 0
for i in range(n):
    maxadd += (100 - skill[i][1]) // 10
ans += min(k // 10, maxadd)
print(ans)
