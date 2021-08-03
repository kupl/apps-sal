n = int(input())
S = []
ans = ''

for i in range(n):
    S.append(str(input()))

data1 = []
data2 = []

for i in range(len(S[0])):
    if not S[0][i] in data1:
        data1.append(S[0][i])
        data2.append(1)
    else:
        data2[data1.index(S[0][i])] += 1

for i in range(1, n):
    for j in range(len(data1)):
        data2[j] = min(data2[j], S[i].count(data1[j]))

for i in range(len(data1)):
    ans += data1[i] * data2[i]

print((''.join(sorted(ans))))
