n = int(input())
f = []
for i in range(n):
    line = list(map(int, input().split()))
    f.append(line)

p = []
for i in range(n):
    line = [int(j) for j in input().split()]
    p.append(line)

res = - 10 ** 11
for i in range(1, 1 << 10):
    tmp_res = 0
    for j in range(n):
        counter = 0
        for k in range(10):
            if i >> k & f[j][k]:
                counter += 1
        tmp_res += p[j][counter]
    res = max(res, tmp_res)

print(res)
