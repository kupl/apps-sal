import sys
input = sys.stdin.readline

n = int(input())
A = tuple(map(int, input().split()))

ANS = 0


def calc(A, ANS, keta):
    if keta == -1:
        return ANS

    Z = []
    O = []

    for a in A:
        if a & (1 << keta) != 0:
            Z.append(a)
        else:
            O.append(a)

    if Z == [] or O == []:
        return calc(A, ANS, keta - 1)

    else:
        return min(calc(Z, ANS + (1 << keta), keta - 1), calc(O, ANS + (1 << keta), keta - 1))


print(calc(A, 0, 30))
