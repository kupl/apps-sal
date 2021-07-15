s = list(input())

n = len(s)
idx = [[-1] for _ in range(26)]
for i in range(n):
    idx[ord(s[i]) - ord('a')].append(i)
for i in range(26):
    idx[i].append(n)

print(min([max([ls[i + 1] - ls[i] for i in range(len(ls) - 1)]) for ls in idx]))

