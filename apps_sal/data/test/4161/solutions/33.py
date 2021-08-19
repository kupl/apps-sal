k = int(input())


def gcd1(a, b):
    while True:
        if a < b:
            (a, b) = (b, a)
        c = a % b
        if c == 0:
            return b
        else:
            a = b
            b = c


count = 0
for i in range(k):
    for j in range(k):
        tmp = gcd1(i + 1, j + 1)
        if tmp == 1:
            count = count + k
        else:
            for l in range(k):
                tmp2 = gcd1(tmp, l + 1)
                count = count + tmp2
print(count)
