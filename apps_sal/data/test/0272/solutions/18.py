(s1, s2) = (input(), input())
(alph1, alph2) = ([], set())
ans = 0
for i in range(len(s1)):
    fff = [max(s1[i], s2[i]), min(s1[i], s2[i])]
    ff = fff not in alph1
    if ff and (s1[i] in alph2 or s2[i] in alph2):
        ans = -1
        break
    elif ff:
        alph1.append(fff)
        if s1[i] != s2[i]:
            ans += 1
    alph2.add(s1[i])
    alph2.add(s2[i])
print(ans)
if ans != -1:
    for i in range(len(alph1)):
        if alph1[i][0] != alph1[i][1]:
            print(alph1[i][0], alph1[i][1])
