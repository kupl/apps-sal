alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = int(input())
li = []
ans = []
STR = ''
for h in range(n):
    li.append([0] * 26)
for i in range(n):
    S = input()
    for j in range(len(S)):
        li[i][alf.index(S[j])] += 1
for k in range(26):
    temp = 1000000000000000000000000000000000000000000
    for l in range(n):
        if temp > li[l][k]:
            temp = li[l][k]
    if temp != 1000000000000000000000000000000000000000000:
        ans.append(temp)
for m in range(26):
    STR = STR + alf[m] * ans[m]
print(STR)
