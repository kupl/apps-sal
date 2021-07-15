import math
import sys
N, K = map(int, input().split())
A = [int(x) for x in input().split()]

MOD = 10**9+7
def modinv(a):
    b = MOD
    u = 1
    v = 0
    while b != 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= MOD
    if u < 0:
        u += MOD
    return u


def solve(N, K, A):
    A = sorted(A, key=lambda x : abs(x))
    #print(A, file=sys.stderr)

    
    if A[N-K] == 0:
        return 0
    Lpos0, Lneg0, Rpos0, Rneg0 = None, None, None, None
    Lneg, Lpos, Rneg, Rpos = 0, 0, 0, 0

    answer0 = 1
    for i in range(N-K, N):
        if A[i] < 0:
            if Rneg == 0:
                Rneg0 = -A[i]
            Rneg += 1
        else:
            if Rpos == 0:
                Rpos0 = A[i]
            Rpos += 1
        answer0 = (answer0 * abs(A[i])) % MOD

    if Rneg % 2 == 0:
        return answer0

    for i in range(N-K)[::-1]:
        if A[i] < 0:
            if Lneg == 0:
                Lneg0 = -A[i]
            Lneg += 1
        else:
            if Lpos == 0:
                Lpos0 = A[i]
            Lpos += 1

    print(f"{K=}",file=sys.stderr)
    #print(f"{Rneg=}, {Rpos=}, {Rneg0=} {Rpos0=}",file=sys.stderr)
    #print(f"{Lneg=}, {Lpos=}, {Lneg0=} {Lpos0=}",file=sys.stderr)
    #print(f"{Lpos0=}, {Lneg0=}, {Rpos0=} {Rneg0=}",file=sys.stderr)

    #    Lpos Lneg Rpos Rneg
    # A  o    O    O    o
    # B  o    O    x    o      / Rneg * Lpos
    # C  x    O    O    o      / Rpos * Lneg
    # B  o    x    O    o
    # B  o    x    x    o
    # D  x    O    x    o
    # D  x    x    o    o
    # D  x    x    x    o
    if (Lpos0 is not None and Rneg0 is not None
        and Rpos0 is not None and Lneg0 is not None):
        answer1 = (answer0 * modinv(Rneg0) % MOD) * Lpos0 % MOD
        answer2 = (answer0 * modinv(Rpos0) % MOD) * Lneg0 % MOD
        print(f"{Lpos0=}, {Lneg0=}, {Rpos0=} {Rneg0=}",file=sys.stderr)

        print(f"{answer1=} {answer2=}", file=sys.stderr)
        print(f"A {Lpos0*Lneg0=} {Rneg0*Rpos0=}", file=sys.stderr)
        if Lpos0 * Rpos0 > Lneg0 * Rneg0:
            print(f"A1 {answer1=}", file=sys.stderr)
            return answer1
        else:
            print(f"A2 {answer2=}", file=sys.stderr)
            return answer2

    if Lpos0 is not None and Rneg0 is not None:
        print("B", file=sys.stderr)
        return  (answer0 * modinv(Rneg0) % MOD) * Lpos0 % MOD
    if Rpos0 is not None and Lneg0 is not None:
        print("C", file=sys.stderr)
        return  (answer0 * modinv(Rpos0) % MOD) * Lneg0 % MOD

    print("D", file=sys.stderr)
    answer0 = 1
    for i in range(K):
        answer0 = (answer0 * A[i]) % MOD
    return answer0


print(solve(N, K, A))
