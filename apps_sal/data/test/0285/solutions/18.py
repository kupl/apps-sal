n = int(input())
(x, y) = list(map(int, input().split()))
(u, v) = ([], [])
x += 1e-07
y -= 1e-07
for i in range(n):
    (k, m) = list(map(int, input().split()))
    u += [(k * x + m, i)]
    v += [(k * y + m, i)]
(u, v) = (sorted(u), sorted(v))
for i in range(n):
    if u[i][1] != v[i][1]:
        print('YES')
        break
else:
    print('NO')
