def chng(c):
    return -1 if c == '-' else (1 if c == '+' else 0)


def f(z, d):
    if z == 0:
        nonlocal al
        al += 1
        if d == 0:
            nonlocal ne
            ne += 1
    else:
        f(z - 1, d - 1)
        f(z - 1, d + 1)


A = input()
B = input()
n = len(A)
x = 0
y = 0
z = 0
for i in range(n):
    x += chng(A[i])
    y += chng(B[i])
    if B[i] == '?':
        z += 1
if z == 0 and x == y:
    print(1)
else:
    d = abs(x - y)
    al = 0
    ne = 0
    f(z, d)
    print(ne / al)
#print(1 / (2 ** (z if z % 2 == 1 else z // 2)))
