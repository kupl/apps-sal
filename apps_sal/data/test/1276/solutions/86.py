n = int(input())
S = list(input())
ans = S.count('R') * S.count('G') * S.count('B')
for i in range(n - 2):
    for j in range(i + 1, (n + i + 1) // 2):
        if S[i] != S[j] and S[j] != S[2 * j - i] and (S[2 * j - i] != S[i]):
            ans -= 1
print(ans)
