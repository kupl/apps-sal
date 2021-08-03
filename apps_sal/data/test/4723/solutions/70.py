S = input()
T = input()
N = len(S)
n = len(T)
ans = []
for i in range(N - n + 1):
    for j in range(n):
        if S[i + j] != T[j] and S[i + j] != '?':
            break
    else:
        s = []
        for j in range(i):
            if S[j] == '?':
                s.append('a')
            else:
                s.append(S[j])
        for j in range(i, i + n):
            s.append(T[j - i])
        for j in range(i + n, N):
            if S[j] == '?':
                s.append('a')
            else:
                s.append(S[j])
        ans.append(''.join(s))

if len(ans) == 0:
    print("UNRESTORABLE")
else:
    ans.sort()
    print((ans[0]))
