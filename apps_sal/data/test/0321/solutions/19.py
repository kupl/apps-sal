t = int(input())
a = []
b = []
for i in range(t):
    (aa, bb) = [int(el) for el in input().split()]
    a.append(aa)
    b.append(bb)


def prost(n):
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    return


for i in range(t):
    if a[i] - b[i] != 1:
        print('NO')
        continue
    if prost(a[i] + b[i]):
        print('YES')
    else:
        print('NO')
