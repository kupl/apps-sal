(n, s) = list(map(int, input().split()))
L = []
for i in range(n):
    (x, y, k) = list(map(int, input().split()))
    L.append((x ** 2 + y ** 2, k))
L.sort()
inc = 0
ind = 0
r = 0
while ind < n and s + inc < 1000000:
    r = L[ind][0]
    inc += L[ind][1]
    ind += 1
if s + inc >= 1000000:
    print(pow(r, 1 / 2))
else:
    print(-1)
