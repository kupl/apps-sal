n = int(input())
a = []
l = []
for i in range(n):
    A = int(input())
    L = [list(map(int, input().split())) for _ in range(A)]
    a.append(A)
    l.append(L)
ans = 0
for i in range(2 ** n):
    b = [0] * n
    for j in range(n):
        if i >> j & 1:
            b[j] = 1
    for k in range(n):
        for h in range(a[k]):
            hito = l[k][h][0] - 1
            singi = l[k][h][1]
            if b[k] == 1 and b[hito] != singi:
                break
        else:
            continue
        break
    else:
        ans = max(ans, sum(b))
print(ans)
