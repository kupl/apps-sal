a00, a01, a10, a11 = list(map(int, input().split()))

if sum([a00, a01, a10, a11]) == 0:
    print(0)
    return

z, j = 0, 0
if a01 != 0 or a10 != 0:
    z = j = 1

while z * (z - 1) // 2 < a00:
    z += 1
while j * (j - 1) // 2 < a11:
    j += 1

if any([z * (z - 1) // 2 != a00,
        j * (j - 1) // 2 != a11,
        z * j != a10 + a01]):
    print('Impossible')
    return

n = z + j
for i in range(n):
    if z > 0 and a01 >= j:
        print('0', end='')
        a01 -= j
        z -= 1
    else:
        print('1', end='')
        j -= 1
