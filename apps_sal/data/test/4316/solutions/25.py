from collections import defaultdict

S = defaultdict(int)
for i in input():
    S[i] += 1

if len(list(S.values())) == 2:
    a, b = list(S.values())
    if a == b == 2:
        print('Yes')
        return
print('No')
