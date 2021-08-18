n = int(input())


def cbt(n):
    b = bin(n)[2:]
    c = 0
    t = 1
    l = []
    while b.count('1') != len(b):
        t ^= 1
        if not t:
            x = int('1' * len(b), 2)
            y = int('0b' + b, 2)
            l.append(len(b))
            b = x ^ y
            b = bin(b)[2:]
        else:
            x = int('0b' + b, 2)
            x += 1
            b = bin(x)[2:]
        c += 1
    return c, l


c, l = cbt(n)
print(c)
print((*l) if l else None)
