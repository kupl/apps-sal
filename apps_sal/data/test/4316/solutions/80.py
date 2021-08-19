s = input()
S = []
for i in range(len(s)):
    S.append(s[i])
B = list(set(S))
cnt1 = 0
cnt2 = 0
if len(B) != 2:
    print('No')
else:
    for i in range(len(s)):
        if B[0] == s[i]:
            cnt1 += 1
        elif B[1] == s[i]:
            cnt2 += 1
    if cnt1 == 2 and cnt2 == 2:
        print('Yes')
    else:
        print('No')
