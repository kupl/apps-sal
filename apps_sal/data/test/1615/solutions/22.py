n, k = input().split()
n, k = int(n), int(k)
L = {""}
for i in range(n):
    m, f = input().split()
    for i in range(int(m), int(f) + 1):
        L |= {i}
L.remove("")
x = len(L)
print((k - x % k) % k)
