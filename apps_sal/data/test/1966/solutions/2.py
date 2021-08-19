from itertools import permutations


def solve(TL, TR, BL, BR, s, n):
    A = []
    for i in range(n):
        X = TL[i].copy()
        X.extend(TR[i])
        A.append(X)
    for i in range(n):
        X = BL[i].copy()
        X.extend(BR[i])
        A.append(X)
    c = 0
    ans = 0
    for i in range(2 * n):
        if i % 2 == 1:
            c = s ^ 1
        else:
            c = s
        for j in range(2 * n):
            if A[i][j] != c:
                ans += 1
                A[i][j] = c
            c ^= 1
    return ans


n = int(input())
P = []
for _ in range(4):
    A = []
    for i in range(n):
        A.append(list(map(int, list(input()))))
    if _ != 3:
        input()
    P.append(A)
ans = 4 * n * n + 1
for S in permutations(range(4)):
    for s in range(2):
        cur = solve(P[S[0]], P[S[1]], P[S[2]], P[S[3]], s, n)
        ans = min(ans, cur)
print(ans)
