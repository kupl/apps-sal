3


def enc(t):
    v = 0
    for x in t:
        v *= 20
        v += x
    return v


def dec(v, N):
    a = []
    for _ in range(N):
        a.append(v % 20)
        v //= 20
    a.reverse()
    return a


def cnt(C, ld, ud):
    N = len(C)
    ans = 0
    dp = {enc([0] * N): 1}
    for rnd in range(ud):
        if rnd >= ld:
            for et in dp:
                c = dp[et]
                t = dec(et, N)
                if C[0] == 0 and all([t[i] >= 1 for i in range(1, N)]) or (C[0] > 0 and all([t[i] >= 1 for i in range(N)])):
                    ans += c
        ndp = {}
        for et in dp:
            t = dec(et, N)
            c = dp[et]
            for i in range(N):
                if rnd == 0 and i == 0:
                    continue
                if t[i] < C[i]:
                    l = list(t)
                    l[i] += 1
                    nt = enc(l)
                    if nt not in ndp:
                        ndp[nt] = 0
                    ndp[nt] += c
        dp = ndp
    for et in dp:
        c = dp[et]
        t = dec(et, N)
        if C[0] == 0 and all([t[i] >= 1 for i in range(1, N)]) or (C[0] > 0 and all([t[i] >= 1 for i in range(N)])):
            ans += c
    return ans


def solve(S):
    N = len(S)
    C = [0] * 10
    for c in S:
        C[ord(c) - ord('0')] += 1
    mindigits = len([c for c in C if c > 0])
    C = [C[0]] + [C[i] for i in range(1, 10) if C[i] > 0]
    return cnt(C, mindigits, N)


def main():
    S = input()
    print(solve(S))


def __starting_point():
    main()


__starting_point()
