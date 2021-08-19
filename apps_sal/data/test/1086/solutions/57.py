(h, w) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [list(map(int, input().split())) for i in range(h)]
s = [0] * w
s[0] = p = 1 << 6400
for i in range(h):
    for j in range(w):
        d = abs(a[i][j] - b[i][j])
        if j > 0:
            s[j] |= s[j - 1]
        s[j] = s[j] << d | s[j] >> d
t = s[-1]
for i in range(6401):
    if t & p << i or t & p >> i:
        print(i)
        break
