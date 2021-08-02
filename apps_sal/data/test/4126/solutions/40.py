S = str(input())
forward = ''
back = ''
for i in range(0, ((len(S) - 1) // 2)):
    forward += S[i]
for j in range(((len(S) + 3) // 2) - 1, len(S)):
    back += S[j]
if forward == back:
    print('Yes')
else:
    print('No')
