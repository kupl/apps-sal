A, B, C = map(int, input().split())


def modder(x):
    ans = int(x % 998244353)
    return ans


A = modder(A)
B = modder(B)
C = modder(C)
resulta = modder(A * (A + 1))
resultb = modder(B * (B + 1))
resultc = modder(C * (C + 1))

resultu = modder(resulta * resultb * resultc)

no = 1
while no:
    if (resultu % 8) != 0:
        resultu = resultu + 998244353
    else:
        no = 0

result = int(resultu / 8)

print(result)
