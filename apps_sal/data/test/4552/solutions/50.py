n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
li = []
for i in range(2 ** 10):
    if i == 0:
        continue
    ans = 0
    co = [0] * n
    for j in range(10):
        if i >> j & 1 == 1:
            for k in range(n):
                if f[k][j] == 1:
                    co[k] += 1
    for l in range(n):
        ans += p[l][co[l]]
    li += [ans]
print(max(li))
