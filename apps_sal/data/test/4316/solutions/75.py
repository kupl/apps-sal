S = input()
s = []
for i in range(4):
    s.append(S[i])
s = set(s)
print('Yes' if len(s) == 2 else 'No')
