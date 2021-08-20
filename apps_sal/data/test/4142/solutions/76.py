S = input()
N = len(S)
ans = 'Yes'
for i in range(N):
    if i % 2 == 0 and S[i] != 'R' and (S[i] != 'U') and (S[i] != 'D') or (i % 2 == 1 and S[i] != 'L' and (S[i] != 'U') and (S[i] != 'D')):
        ans = 'No'
        break
print(ans)
