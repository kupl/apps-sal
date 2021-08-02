n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cands = {}
aux = 0
zero = 0


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


for i in range(n):
    if b[i] == 0 and a[i] == 0:
        aux += 1
    elif a[i] != 0:

        if a[i] < 0:
            a_semn = -1
            a[i] = -a[i]
        else:
            a_semn = +1

        if b[i] < 0:
            b_semn = -1
            b[i] = -b[i]
        else:
            b_semn = +1

        if b[i] != 0:
            cmmdc = gcd(a[i], b[i])
            a_redus = a[i] // cmmdc
            b_redus = b[i] // cmmdc
        else:
            a_redus = a[i]
            b_redus = b[i]
            zero += 1

        c_semn = a_semn * b_semn

        cands[(a_redus, b_redus, c_semn)] = cands.get((a_redus, b_redus, c_semn), 0) + 1

cmax = 0
for i in cands:
    if cands[i] > cmax:
        cmax = cands[i]

print(aux + max(cmax, zero))
