N = int(input())
S = input()
ans = S.count('R') * S.count('G') * S.count('B')
for i in range(1, N - 1):
    for j in range(i + 1, N):
        k = 2 * j - i
        if k > N:
            break
        if S[i - 1] != S[j - 1] and S[j - 1] != S[k - 1] and (S[k - 1] != S[i - 1]):
            ans -= 1
print(ans)
