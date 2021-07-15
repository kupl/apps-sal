S = list(input())
ans = 'No'
if (S[0] == S[1] and S[0] != S[2] and S[2] == S[3]) or (S[0] == S[2] and S[0] != S[1] and S[1] == S[3]) or (S[0] == S[3] and S[0] != S[1] and S[1] == S[2]):
    ans = 'Yes'
print(ans)
