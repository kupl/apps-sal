ans = 'No'
S = input()
initial = S[0]
SS = S.replace(initial, '')
if len(SS) == 2:
    if SS[0] == SS[1]:
        ans = 'Yes'
print(ans)
