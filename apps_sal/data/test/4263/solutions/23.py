S = input()
max_ = 0
for i in range(len(S)):
    for j in range(i, len(S)):
        if all(('ACGT'.count(c) == 1 for c in S[i:j + 1])):
            max_ = max(j + 1 - i, max_)
print(max_)
