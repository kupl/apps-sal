S = input()
S = S.replace('A', 'a')
S = S.replace('T', 'a')
S = S.replace('C', 'a')
S = S.replace('G', 'a')
ans = 0
x = 0
for i in range(len(S)):
    if S[i] == 'a':
        x += 1
    else:
        if ans < x:
            ans = x
        x = 0
if ans < x:
    ans = x
print(ans)
