n, m = list(map(int, input().split()))
d = [0] * m
s = list(list(map(int, input())) for i in range(n))
for x in s:
    for i in range(m):
        d[i] += x[i]
for x in s:
    f = 1
    for i in range(m):
        if x[i]:
            if d[i] == 1:
                f = 0
                break
    if f:
        print('YES')
        return
print('NO')

