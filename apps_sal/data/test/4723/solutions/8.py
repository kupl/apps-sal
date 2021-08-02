import copy
S = list(input())
T = input()
lS = len(S)
lT = len(T)
ans = []
for s in range(lS - lT + 1):
    temp = copy.copy(S)
    for t in range(lT):
        if temp[s + t] != T[t] and temp[s + t] != '?':
            break
        else:
            temp[s + t] = T[t]
    else:
        temp = [temp[i] if temp[i] != '?' else 'a' for i in range(lS)]
        ans.append(''.join(temp))
ans = sorted(ans)
if len(ans) == 0:
    print('UNRESTORABLE')
else:
    print(ans[0])
