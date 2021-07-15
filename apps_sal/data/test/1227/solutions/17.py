import math
n = int(input())
K = int(input())

def calk1(n):
    if n == 0: return 0
    m = int(math.log10(n))
    num = m * 9
    num += n//(10**m)
    return num

def calk2(n):
    m = int(math.log10(n))
    num = m * (m - 1) // 2 * 9**2
    num += (n//(10**m)-1) * m * 9
    num += calk1(n - (n//(10**m)*10**m))
    return num

def calk3(n):
    m = int(math.log10(n))
    num = m * (m - 1) * (m - 2) // 6 * 9**3
    num += (n//(10**m)-1) * (m * (m - 1) // 2 * 9**2)
    num += calk2(n - (n//(10**m)*10**m))
    return num
if n < 10 ** (K - 1): print((0))
else:
    if K == 1: print((calk1(n)))
    elif K == 2: print((calk2(n)))
    else: print((calk3(n)))

