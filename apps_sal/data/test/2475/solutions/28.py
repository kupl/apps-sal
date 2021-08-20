N = int(input())
S = list(map(int, input().split()))
ans = 0
for C in range(1, N):
    fkC = 0
    L = 0
    R = N - 1
    if (N - 1) % C == 0:
        while L < R:
            fkC += S[L] + S[R]
            ans = max(ans, fkC)
            L += C
            R -= C
    else:
        while L + C < N - 1:
            fkC += S[L] + S[R]
            ans = max(ans, fkC)
            L += C
            R -= C
print(ans)
