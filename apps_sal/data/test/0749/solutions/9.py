a = input()

S = [[-1] for i in range(26)]

for i in range(len(a)):
    S[ord(a[i]) % 97] += [i]
for i in range(len(S)):
    S[i] += [len(a)]
min = [-1 for i in range(26)]
# print(S)
for i in range(26):
    for j in range(1, len(S[i])):
        if min[i] < S[i][j] - S[i][j - 1]:
            min[i] = S[i][j] - S[i][j - 1]
m = 10**6
for i in min:
    if i != -1 and i < m:
        m = i
print(m)
