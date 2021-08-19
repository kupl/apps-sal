(n, k) = map(int, input().split())
b = [bi - 1 for bi in list(map(int, input().split()))]
a = 0
f = [0] * n
c = 1
for i in range(k):
    if f[a]:
        k %= c - f[a]
        for i in range(k):
            a = b[a]
        print(a + 1)
        break
    f[a] = c
    k -= 1
    c += 1
    a = b[a]
else:
    print(a + 1)
