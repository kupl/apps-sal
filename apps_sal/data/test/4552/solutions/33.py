from itertools import product
n = int(input())
f = []
for i in range(n):
    f.append(list(map(int, input().split())))
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

schejule_list = set(product([0, 1], repeat=10))
ans = - float("inf")
for schedule in schejule_list:
    if schedule == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
        continue
    res = 0
    for i in range(n):
        kaburi = 0
        for j in range(10):
            kaburi += f[i][j] * schedule[j]
        res += p[i][kaburi]
    ans = max(ans, res)
print(ans)
