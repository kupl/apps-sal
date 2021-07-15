MOD = pow(10,9)+7
def MODINV(n:int, MOD=MOD):
    return pow(n, MOD-2, MOD)

def main():
    N = int(input())
    S1 = input()
    S2 = input()
    ans = 1; i = 0
    M = (S1[-1] == S2[-1]) * N + (S1[-1] != S2[-1]) * (N-1)
    for _ in range(N):
        if i >= M-1:
            break
        s1 = S1[i]
        s2 = S2[i]
        if s1 == s2:
            ans *= 2
            i += 1
        else:
            if S1[i+2] != S2[i+2]:
                ans *= 3
            i += 2
        ans %= MOD

    if S1[0] == S2[0]:
        ans *= 3
    else:
        ans *= 6
    print((ans%MOD))

def __starting_point():
    main()

__starting_point()
