N = int(input())
S = input()
(cntR, cntG, cntB) = (S.count('R'), S.count('G'), S.count('B'))
ans = cntR * cntG * cntB
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if S[i] != S[j]:
            k = 2 * j - i
            if k < N and S[k] != S[i] and (S[k] != S[j]):
                ans -= 1
print(ans)
