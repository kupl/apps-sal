S = input()
T = input()
d = [[] for i in range(26)]
for (i, c) in enumerate(S):
    d[ord(c) - ord('a')].append(i)
d2 = [[] for i in range(26)]
for (i, c) in enumerate(T):
    d2[ord(c) - ord('a')].append(i)
print(['No', 'Yes'][set((tuple(x) for x in d)) == set((tuple(x) for x in d2))])
