import sys
input = sys.stdin.readline

n, q = list(map(int, input().split()))
X = list(range(1, n + 1))

S = [0]
for x in X:
    S.append(S[-1] + x)

FACT = [1, 1]
for i in range(2, 16):
    FACT.append(FACT[-1] * i)

A = X[-15:]
LEN = len(A)


def calc(x):
    AA = [a for a in A]
    ANS = []

    for i in range(LEN, 0, -1):
        q = x // FACT[i - 1]
        x -= q * FACT[i - 1]

        ANS.append(AA.pop(q))

        # print(q,x,AA,ANS)

    return ANS


NOW = 0
for queries in range(q):
    Q = list(map(int, input().split()))

    if Q[0] == 2:
        NOW += Q[1]
        continue

    l, r = Q[1], Q[2]

    if r <= n - LEN:
        print(S[r] - S[l - 1])
        continue

    elif l <= n - LEN:
        ANS = S[-LEN - 1] - S[l - 1]
        l = 0
        r -= n - LEN + 1
    else:
        ANS = 0
        l -= n - LEN + 1
        r -= n - LEN + 1

    NOWA = calc(NOW)

    print(ANS + sum(NOWA[l:r + 1]))
