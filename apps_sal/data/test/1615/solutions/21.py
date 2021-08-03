n, k = map(int, input().split())
L = {""}
for i in range(n):
    m, f = map(int, input().split())
    for i in range(m, f + 1):
        L |= {i}
L.remove("")
x = len(L)
print((k - x % k) % k)
