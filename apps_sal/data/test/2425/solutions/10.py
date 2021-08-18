def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def f(a):
    best = -1
    tag = None

    for b in range(1, a):
        d = gcd(a ^ b, a & b)
        if d > best:
            best = d
            tag = b
    return best, tag


def f2(a):
    for b in range(a - 1, 0, -1):
        if a % b == 0:
            return b


special = dict()


special = {3: 1, 7: 1, 15: 5, 31: 1, 63: 21, 127: 1, 255: 85, 511: 73, 1023: 341, 2047: 89, 4095: 1365, 8191: 1, 16383: 5461, 32767: 4681, 65535: 21845, 131071: 1, 262143: 87381, 524287: 1, 1048575: 349525, 2097151: 299593, 4194303: 1398101, 8388607: 178481, 16777215: 5592405, 33554431: 1082401}

q = int(input())

for test in range(q):
    a = int(input())
    if a in special:
        print(special[a])
    else:
        length = len(bin(a)) - 2
        print(2**length - 1)
