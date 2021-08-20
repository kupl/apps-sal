N = int(input())
S = input()
S = 'N' + S + 'N'
ans = 0
E = 0
W = S.count('W')
for i in range(1, N + 1):
    if S[i - 1] == 'E':
        E += 1
    if S[i] == 'W':
        W -= 1
    tmp = E + W
    if tmp > ans:
        ans = tmp
ans = N - 1 - ans
print(ans)
