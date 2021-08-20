def solve():
    S = input()
    T = input()
    N = len(S)
    M = 2 * N
    S += S
    nxt = [[M] * 26 for i in range(M + 1)]
    for i in range(M - 1, -1, -1):
        for j in range(26):
            nxt[i][j] = nxt[i + 1][j]
        nxt[i][ord(S[i]) - ord('a')] = i
    ans = 0
    i = 0
    for c in T:
        pos = ord(c) - ord('a')
        if nxt[i][pos] == M:
            return -1
        ans += nxt[i][pos] - i + 1
        i = (nxt[i][pos] + 1) % N
    return ans


print(solve())
