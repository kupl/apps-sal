N = int(input())
S = list(input())
ans = S.count('R') * S.count('G') * S.count('B')
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = j * 2 - i
        if k >= N:
            break
        if S[i] != S[j] and S[i] != S[k] and (S[j] != S[k]):
            ans -= 1
print(ans)
