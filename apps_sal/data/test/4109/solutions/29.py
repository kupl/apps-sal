# 他の人の回答
n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

add = []

for i in range(2**n):
    skill = [0] * (m + 1)
    for j in range(n):
        if ((i >> j) & 1):
            skill = list(map(sum, zip(skill, ca[j])))
    if min(skill[1:]) >= x:
        add.append(skill)

if add:
    add.sort()
    print(add[0][0])
else:
    print(-1)
