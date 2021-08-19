N, M, X = list(map(int, input().split()))
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

d = []

for i in range(1 << N):
    s = [0] * M
    c = 0
    for j in range(N):
        if (i >> j) & 1:
            # print(j, "entry")
            for k in range(M):
                s[k] += a[j][k + 1]
            c += a[j][0]

    # print(s, c, d)

    b = True
    for ii in s:
        if ii < X:
            b = False
    if b:
        d.append(c)

if len(d) == 0:
    print("-1")
else:
    print((min(d)))
