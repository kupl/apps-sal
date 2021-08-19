from collections import Counter
S = input()
C = Counter(S)
L = len(S)
A = C['a']
print(min(A * 2 - 1, L))
