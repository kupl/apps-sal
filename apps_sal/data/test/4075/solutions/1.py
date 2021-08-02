n, m = map(int, input().split())
f = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
count = 0
for i in range(2**n):
    Bit = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            Bit[j] = 1
    same = 0
    for k in range(m):
        sum = 0
        for l in range(f[k][0]):
            if Bit[f[k][l + 1] - 1] == 1:
                sum += 1
        if sum % 2 != p[k]:
            break
    else:
        count += 1
print(count)
