(N, M) = map(int, input().split())
a = M // 2
b = M - a
c = 1
d = 2 * a + 1
for i in range(a):
    print(c, d)
    c += 1
    d -= 1
e = 2 * a + 2
f = 2 * M + 1
for i in range(b):
    print(e, f)
    e += 1
    f -= 1
