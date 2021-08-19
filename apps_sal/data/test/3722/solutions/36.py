N = int(input())
cAA = input()
cAB = input()
cBA = input()
cBB = input()
mod = 10 ** 9 + 7


def ans(value):
    print(value)
    return


def dp():
    nA = 1
    nB = 0
    for i in range(N - 3):
        (nA, nB) = ((nA + nB) % mod, nA)
    return (nA + nB) % mod


if N <= 3:
    ans(1)
if cAA == 'A' and cBB == 'B':
    ans(1)
if cAA == cBB:
    if cAA == cAB:
        ans(1)
    if cAB == cBA:
        ans(dp())
    ans(pow(2, N - 3, mod))
if cAB == cBA:
    ans(dp())
ans(pow(2, N - 3, mod))
