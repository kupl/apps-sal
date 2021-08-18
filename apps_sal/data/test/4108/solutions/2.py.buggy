S = input()
T = input()

chk1 = [[] for _ in range(26)]
chk2 = [[] for _ in range(26)]
for i in range(len(S)):
    s1 = ord(S[i]) - 97
    s2 = ord(T[i]) - 97
    if len(chk1[s1]) == 0:
        chk1[s1].append(T[i])
    else:
        if chk1[s1][0] == T[i]:
            pass
        else:
            print('No')
            return
    if len(chk2[s2]) == 0:
        chk2[s2].append(S[i])
    else:
        if chk2[s2][0] == S[i]:
            pass
        else:
            print('No')
            return
print('Yes')
