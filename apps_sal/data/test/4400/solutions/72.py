S = input()
ans = 0
if 'R' in S:
    if S[0] == S[1] or S[1] == S[2]:
        ans = S.count('R')
    else:
        ans += 1
print(ans)
