n, k = map(int, input().split())
L = {""}
for i in range(n):
    m, f = input().split()
    for i in range(int(m), int(f) + 1):
        L |= {i}
L.remove("")
x = len(L)
if x % k == 0:
    print("0")
else:
    print(k - x % k)
