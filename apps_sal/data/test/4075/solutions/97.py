n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
count = 0
for i in range(2 ** n):
    on_number = [0] * m
    for j in range(n):
        if i >> j & 1:
            for k in range(m):
                if (j + 1) in s[k][1:]:
                    on_number[k] += 1
    flag = 0
    for k in range(m):
        if on_number[k] % 2 == p[k]:
            flag += 1
        if flag == m:
            count += 1
print(count)
