def res(d, N):
    for i in range(1, N):
        if d[i][1] <= d[i - 1][1]:
            return str(d[i][2] + 1) + ' ' + str(d[i - 1][2] + 1)
    return '-1 -1'


N = int(input())
d = []
for i in range(N):
    (a, b) = list(map(int, input().split()))
    d.append((a, b, i))
d = sorted(d, key=lambda x: (x[0], -x[1]))
print(res(d, N))
