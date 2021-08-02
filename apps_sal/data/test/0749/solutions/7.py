s = str(input())
s = list(s)
n = len(s)
S = set(s)
S = list(S)
N = len(S)
l = [[] for i in range(N)]
r = [-1 for i in range(N)]
for i in range(n):
    for j in range(N):
        if s[i] == S[j]:
            l[j].append(i)
            break
for i in range(N):
    l[i] = [-1] + l[i] + [n]
for i in range(N):
    for j in range(1, len(l[i])):
        r[i] = max(r[i], l[i][j] - l[i][j - 1])
print(min(r))
