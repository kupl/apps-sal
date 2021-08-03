n, m = list(map(int, input().split()))

ans = []

re = [[] for _ in range(n)]


for _ in range(m):
    a = list(map(int, input().split()))
    re[a[0] - 1].append(a[1])
    ans.append(a)

d = {}
for f in re:
    new = sorted(f)

    for i in range(len(new)):
        d[new[i]] = i + 1

for x in ans:
    p = x[0]
    q = d[x[1]]
    print((str('{:0=6}'.format(p)) + str('{:0=6}'.format(q))))
