S = input()
T = input()
s_len = len(S)
t_len = len(T)
res = []
init_K = '?' * s_len
for i in range(s_len - t_len + 1):
    K = list(init_K[:i] + T + init_K[i + t_len:])
    for j in range(s_len):
        if S[j] == '?' or S[j] == K[j]:
            pass
        elif K[j] == '?':
            K[j] = S[j]
        else:
            break
    else:
        res.append(''.join(K).replace('?', 'a'))
if res:
    res.sort()
    print(res[0])
else:
    print('UNRESTORABLE')
