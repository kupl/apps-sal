n = int(input())
l = input()
r = input()
s = 'abcdefghijklmnopqrstuvwxyz'
d1 = {}
d2 = {}
for c in s:
    d1[c] = []
    d2[c] = []
d1['?'] = []
d2['?'] = []
for i in range(n):
    d1[l[i]].append(i)
    d2[r[i]].append(i)
ansleft = []
ansright = []
checkedleft = [0 for i in range(n)]
checkedright = [0 for j in range(n)]
for j in range(26):
    let = s[j]
    l1 = list(d1[let])
    l2 = list(d2[let])
    c1 = len(l1)
    c2 = len(l2)
    cnt = min(c1, c2)
    i = 0
    while i < cnt:
        ansleft.append(l1[i])
        ansright.append(l2[i])
        checkedright[l2[i]] = 1
        checkedleft[l1[i]] = 1
        i += 1
nonques1 = []
nonques2 = []
ques1 = list(d1['?'])
ques2 = list(d2['?'])
for i in range(n):
    if l[i] != '?' and checkedleft[i] == 0:
        nonques1.append(i)
    if r[i] != '?' and checkedright[i] == 0:
        nonques2.append(i)
j = 0
k = 0
for i in range(len(ques1)):
    if ques1[i] != -1:
        if j < len(nonques2):
            ansleft.append(ques1[i])
            ansright.append(nonques2[j])
            nonques2[j] = -1
            j += 1
            ques1[i] = -1
        elif k < len(ques2):
            ansleft.append(ques1[i])
            ansright.append(ques2[k])
            ques2[k] = -1
            k += 1
            ques1[i] = -1
j = 0
k = 0
for i in range(len(ques2)):
    if ques2[i] != -1:
        if j < len(nonques1):
            ansright.append(ques2[i])
            ansleft.append(nonques1[j])
            nonques1[j] = -1
            j += 1
            ques2[i] = -1
        elif k < len(ques1):
            ansright.append(ques2[i])
            ansleft.append(ques1[k])
            ques1[k] = -1
            k += 1
            ques2[i] = -1
print(len(ansleft))
for i in range(len(ansleft)):
    print(ansleft[i] + 1, ansright[i] + 1)
