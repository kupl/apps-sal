S = input()
res = False
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        res = True
print(['Good', 'Bad'][res])
