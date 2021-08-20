q = int(input())
q -= 1
(a, s) = list(map(int, input().split()))
if s == 1:
    z = 1900
    x = 9000000000
else:
    z = -9000000000
    x = 1899
z += a
x += a
for j in range(0, q):
    (a, s) = list(map(int, input().split()))
    if s == 1:
        z = max(1900, z)
    else:
        x = min(1899, x)
    z += a
    x += a
if x < z:
    print('Impossible')
elif x >= 7000000000:
    print('Infinity')
else:
    print(x)
