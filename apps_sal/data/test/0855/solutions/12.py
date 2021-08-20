def R():
    return list(map(int, input().split()))


(k, a, b) = R()
a -= 1
b -= 1
A = [list(R()) for _ in range(3)]
B = [list(R()) for _ in range(3)]
f = [[None] * 3 for _ in range(3)]
s = [[0, 0]]
i = 0
while i < k and f[a][b] is None:
    f[a][b] = i
    s.append(list(s[i]))
    i += 1
    d = a - b
    if d < 0:
        d += 3
    if d:
        s[i][d - 1] += 1
    (a, b) = (A[a][b] - 1, B[a][b] - 1)
if i == k:
    print(*s[i])
else:
    j = f[a][b]
    (c, d) = divmod(k - i, i - j)
    z = list(zip(s[i], s[j], s[j + d]))
    print(*[(c + 1) * (x[0] - x[1]) + x[2] for x in z])
