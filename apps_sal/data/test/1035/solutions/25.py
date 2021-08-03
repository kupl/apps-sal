import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


A, B = map(int, input().split())
Af = factorization(A)
Bf = factorization(B)
As = set()
Bs = set()
for i in range(len(Af)):
    As.add(Af[i][0])
for j in range(len(Bf)):
    Bs.add(Bf[j][0])
if A == 1 and B == 1:
    print(1)
else:
    print(len(As & Bs) + 1)
