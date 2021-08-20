S = input()
T = input()
ans = 1
for i in range(len(S)):
    if S[i] != T[i]:
        ans = 0
        break
if ans == 1:
    print('Yes')
else:
    print('No')
