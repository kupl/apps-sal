import math


def f(perm):
    a1 = 0
    a2 = 0
    for i in range(len(perm) // 2):
        a1 += abs(perm[2 * i] - perm[2 * i + 1])
    for i in range(len(perm)):
        if i % 2 == 0:
            a2 += perm[i]
        else:
            a2 -= perm[i]
    a2 = abs(a2)
    return (a1 - a2) // 2


perm = [7, 1, 2, 3, 4, 5, 6, 8, 9, 10]
# print(f(perm))
n, k = list(map(int, input().split(' ')))

res = []

if k == 0:
    for i in range(1, 2 * n + 1):
        res.append(i)
    print(res.__str__().replace(",", "").replace("[", "").replace("]", ""))
    return

if n % 2 == 0:
    znak = 1 + k
else:
    if k == n:
        znak = k + 2
    else:
        znak = k + 1

res.append(znak)
res.append(1)
pointer = 2

if pointer == znak:
    pointer += 1

for i in range(n - 1):
    a = pointer

    pointer += 1
    if pointer == znak:
        pointer += 1

    b = pointer

    pointer += 1
    if pointer == znak:
        pointer += 1

    res.append(a)
    res.append(b)

print(res.__str__().replace(",", "").replace("[", "").replace("]", ""))
