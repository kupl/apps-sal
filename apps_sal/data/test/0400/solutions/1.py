import sys


#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

n, k = [int(i) for i in input().split()]
skill = [[int(i) % 10, int(i)] for i in input().split()]

skill.sort(reverse=True)
ans = 0
for i in range(n):
    ans += skill[i][1] // 10
# print(skill)
# print(k)
for i in range(n):
    if skill[i][1] == 100:
        continue
    toup = 10 - skill[i][0]
    if k >= toup:
        k -= toup
        ans += 1
        skill[i][1] += toup

# print(skill)

maxadd = 0
for i in range(n):
    maxadd += (100 - skill[i][1]) // 10
# print(maxadd)
ans += min(k // 10, maxadd)
print(ans)
