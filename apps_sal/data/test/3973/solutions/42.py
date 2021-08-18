def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (2 * M + 3)
    for i in range(N - 1):
        now = A[i]
        nex = A[i + 1]
        L = nex - now
        if L - 1 > 0:
            S[now + 2] += 1
            S[nex + 1] += -L
            S[nex + 2] += L - 1
        elif L < 0:
            L = L % M
            if L - 1 > 0:
                S[now + 2] += 1
                S[nex + 1 + M] += -L
                S[nex + 2 + M] += L - 1
    for i in range(2 * M + 2):
        S[i + 1] += S[i]
    for i in range(2 * M + 2):
        S[i + 1] += S[i]
    B = [0] * (M + 1)
    for i in range(1, M + 1):
        B[i] = S[i] + S[i + M]
    X = 1
    diff = 0
    for i in range(1, M + 1):
        if B[i] > diff:
            diff = B[i]
            X = i
    SS = 0
    for i in range(N - 1):
        SS += (A[i + 1] - A[i]) % M
    print(SS - diff)


main()
