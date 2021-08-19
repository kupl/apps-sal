N = int(input())
S = input()
alf = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
for i in range(N - 1):
    S1 = list(S[0:i + 1])
    S2 = list(S[i + 1:N])
    temp = 0
    li1 = [0] * 26
    li2 = [0] * 26
    for j in range(len(S1)):
        li1[alf.find(S1[j])] += 1
    for k in range(len(S2)):
        li2[alf.find(S2[k])] += 1
    for l in range(26):
        if min(li1[l], li2[l]) != 0:
            temp += 1
    if temp > ans:
        ans = temp
print(ans)
