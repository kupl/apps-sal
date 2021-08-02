n = int(input())
MAT = [format(int(input(), 16), "b").zfill(n) for i in range(n)]

R = []

NOW = 1
for i in range(1, n):
    if MAT[i] == MAT[i - 1]:
        NOW += 1
    else:
        R.append(NOW)
        NOW = 1

R.append(NOW)

C = []


def matchcol(i):
    for j in range(n):
        if MAT[j][i - 1] != MAT[j][i]:
            return 0
    else:
        return 1


NOW = 1
for i in range(1, n):
    if matchcol(i):
        NOW += 1
    else:
        C.append(NOW)
        NOW = 1

C.append(NOW)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


ANS = R[0]
for x in R + C:
    ANS = gcd(ANS, x)

print(ANS)
