S = list(input())
T = input()
candidate = []

ans = True
for i in range(len(S)):
    flag = True
    for j in range(len(T)):
        if i + j >= len(S):
            flag = False
            break
        if S[i+j] == '?' or S[i+j] == T[j]:
            pass
        else:
            flag = False
            break
    if flag:
        candidate.append(i)
        ans = False

if ans:
    print('UNRESTORABLE')
    return

i = candidate[-1]
for tmp in range(i, i + len(T)):
    S[tmp] = T[tmp-i]


for i in range(len(S)):
    if S[i] == '?':
        S[i] = 'a'

print(''.join(S))
