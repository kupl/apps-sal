(a, b) = map(int, input().split())
n = list(map(int, input().split()))
x = 0
z = 100000
i = 0
while i < a:
    if n[i] > x:
        x = n[i]
    i += 1
k = [0] * x
i = 0
while i < a:
    k[n[i] - 1] += 1
    i += 1
i = x - 1
j = 1
z = 0
c = b
while i > -1:
    if k[i] + z == a:
        break
    if k[i] + z <= c:
        c -= k[i] + z
    else:
        c = b - k[i] - z
        j += 1
    z += k[i]
    i -= 1
if k[x - 1] == a:
    print(0)
else:
    print(j)
