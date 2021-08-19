S = input()
ls = []
check = True
for i in range(len(S)):
    if S[i] in ls:
        check = False
        break
    ls.append(S[i])
print('yes' if check else 'no')
