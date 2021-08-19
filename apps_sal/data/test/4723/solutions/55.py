S = input()
T = input()
n = len(S)
l = len(T)
for i in range(n - l + 1)[::-1]:
    cnt = 0
    for j in range(l):
        if S[i + j] == '?' or S[i + j] == T[j]:
            cnt += 1
    if cnt == l:
        S = list(S[:i] + T + S[i + l:])
        for k in range(n):
            if S[k] == '?':
                S[k] = 'a'
        print(''.join(S))
        break
else:
    print('UNRESTORABLE')
