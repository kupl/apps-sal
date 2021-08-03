n = int(input())
a = []
x = []
for _ in range(n):
    A = int(input())
    X = [list(map(int, input().split())) for _ in range(A)]
    a.append(A)
    x.append(X)
ans = 0

for i in range(2**n):
    tmp = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            tmp[j] = 1
    for k in range(n):
        for h in range(a[k]):
            hito = x[k][h][0] - 1
            singi = x[k][h][1]
            if tmp[k] == 1:
                if tmp[hito] != singi:
                    break
        else:
            continue
        break  # https://note.nkmk.me/python-break-nested-loops/
    else:
        ans = max(ans, sum(tmp))

print(ans)
