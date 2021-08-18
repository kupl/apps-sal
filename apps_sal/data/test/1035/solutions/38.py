def gcd(a, b):
    while a % b != 0:
        return gcd(b, a % b)
    return b


A, B = (int(x) for x in input().split())

Gcd = gcd(A, B)
lo_cds = []
up_cds = []
i = 1
while i * i <= Gcd:
    if Gcd % i == 0:
        lo_cds.append(i)
        if Gcd // i != i:
            up_cds.append(Gcd // i)
    i += 1
Cds = lo_cds + up_cds[::-1]
Cds.pop(0)
i = 0


while i < len(Cds):
    j = i + 1
    while j < len(Cds):
        if Cds[j] % Cds[i] == 0:
            Cds.pop(j)
        else:
            j += 1
    i += 1

print(len(Cds) + 1)
