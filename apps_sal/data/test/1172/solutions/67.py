S = input()
MOD = 10 ** 9 + 7
A = 0
AB = 0
ABC = 0
cnt = 1
for c in S:
    if c == 'A':
        A += cnt
        A %= MOD
    elif c == 'B':
        AB += A
        AB %= MOD
    elif c == 'C':
        ABC += AB
        ABC %= MOD
    else:
        nA = 3 * A + cnt
        nAB = 3 * AB + A
        nABC = 3 * ABC + AB
        cnt *= 3
        (A, AB, ABC) = (nA % MOD, nAB % MOD, nABC % MOD)
        cnt %= MOD
print(ABC)
