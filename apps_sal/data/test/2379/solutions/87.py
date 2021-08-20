(N, K, C) = map(int, input().split())
S = list(input())
S_work = []
s = []
f = []
i = 0
while len(s) < K:
    if S[i] == 'o':
        s.append(i)
        i += C + 1
    elif S[i] == 'x':
        i += 1
    elif i == len(S):
        break
i = 1
while len(f) < K:
    if S[N - i] == 'o':
        f.append(N - i)
        i += C + 1
    elif S[N - i] == 'x':
        i += 1
    elif i == len(S):
        break
f.sort()
for i in range(K):
    if s[i] == f[i]:
        print(s[i] + 1)
