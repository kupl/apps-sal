a, b = input().split()
n = int(a)
m = int(b)
t = ["" for j in range(n)]
for i in range(n):
    t[i] = input()
v = 0


def test(a, b, c, d):
    g = [0 for i in range(200)]
    g[ord(a)] += 1
    g[ord(b)] += 1
    g[ord(c)] += 1
    g[ord(d)] += 1
    return (g[ord('f')] * g[ord('a')] * g[ord('c')] * g[ord('e')] == 1)


for i in range(n - 1):
    for j in range(m - 1):
        if test(t[i][j], t[i + 1][j], t[i][j + 1], t[i + 1][j + 1]): v += 1
print(v)
