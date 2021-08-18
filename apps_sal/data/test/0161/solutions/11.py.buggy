x = int(input())

O = []
nop = 0


def opA(x, n):
    nonlocal nop
    nop += 1
    O.append(n)
    r = x ^ ((1 << n) - 1)
    return r


def opB(x):
    nonlocal nop
    nop += 1
    return x + 1


def islc(x):
    b = '{:b}'.format(x)
    return b.count('0') == 0


for i in range(20):
    b = '{:b}'.format(x)
    n = len(b)
    o = n - b.find('0')
    x = opA(x, o)
    if islc(x):
        break
    x = opB(x)
    if islc(x):
        break

print(nop)
print(*O)
