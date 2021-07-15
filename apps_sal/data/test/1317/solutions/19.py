a, b = map(int, input().split())
A = set()
A_ = set()
B_ = set()
A__ = {}
B__ = {}
calc = 0
for i in range(1, b + 1):
    for j in range(1, b + 1):
        if (i ** 2 + j ** 2) % b == 0:
            A.add((i % b, j % b))
            B_.add(j % b)
            A_.add(i % b)
for i in A_:
    A__[i] = a // b
    if a % b >= i and i != 0:
        A__[i] += 1
for i in B_:
    B__[i] = a // b
    if a % b >= i and i != 0:
        B__[i] += 1
for i in A:
    calc += A__[i[0]] * B__[i[1]]
print(calc)
