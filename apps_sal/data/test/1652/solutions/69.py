S = input().strip()
L = len(S)
poss = [False for _ in range(L + 1)]
poss[0] = True
wds = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(L):
    if not poss[i]:
        continue
    for s in wds:
        if i + len(s) <= L:
            if S[i:i + len(s)] == s:
                poss[i + len(s)] = True
if poss[L]:
    print('YES')
else:
    print('NO')
