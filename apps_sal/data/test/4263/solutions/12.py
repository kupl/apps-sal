S = input()
d = ['A', 'T', 'C', 'G']
l = len(S)
acgt = []
a = ''
for i in range(l):
    if S[i] in d:
        a = a + S[i]
        if i == l - 1:
            acgt.append(a)
    else:
        acgt.append(a)
        a = ''
max = 0
for a in acgt:
    if len(a) > max:
        max = len(a)
print(max)
