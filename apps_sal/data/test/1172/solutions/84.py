S = input()


def solve(S):
    mod = 10**9 + 7
    N = len(S)
    Aquest = []
    Cquest = []
    cntA, cntquest = 0, 0
    for i in range(N):
        if S[i] in 'B?':
            Aquest.append([cntA, cntquest])
        if S[i] == 'A':
            cntA += 1
        if S[i] == '?':
            cntquest += 1
    cntC, cntquest = 0, 0
    for i in range(N - 1, -1, -1):
        if S[i] in 'B?':
            Cquest.append([cntC, cntquest])
        if S[i] == 'C':
            cntC += 1
        if S[i] == '?':
            cntquest += 1
    Cquest = Cquest[::-1]
    ans = 0
    for aquest, cquest in zip(Aquest, Cquest):
        a = aquest[0] * pow(3, aquest[1], mod)
        if aquest[1] > 0:
            a += aquest[1] * pow(3, aquest[1] - 1, mod)
        c = cquest[0] * pow(3, cquest[1], mod)
        if cquest[1] > 0:
            c += cquest[1] * pow(3, cquest[1] - 1, mod)
        ans += a * c % mod
    ans %= mod
    return ans


print(solve(S))
