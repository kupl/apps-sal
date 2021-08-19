from collections import Counter
N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)
S = Counter(S)
print(len(S))
