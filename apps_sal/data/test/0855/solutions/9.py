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
    cb = f[a][b]
    c = i - cb
    m = (k - i) // c
    (sa, sb) = s[i]
    sa += m * (sa - s[cb][0]) + s[cb + (k - i) % c][0] - s[cb][0]
    sb += m * (sb - s[cb][1]) + s[cb + (k - i) % c][1] - s[cb][1]
    print(sa, sb)
