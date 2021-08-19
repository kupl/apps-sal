S = input()
T = input()
yes = True
l = len(S)
for i in range(0, l):
    if S[i] != T[i]:
        yes = False
        break
if yes:
    print('Yes')
else:
    print('No')
