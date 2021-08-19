S = input()
cnt = 0
for i in range(0, len(S)):
    if i % 2 == 0:
        if S[i] in ['R', 'U', 'D']:
            cnt += 1
    elif S[i] in ['L', 'U', 'D']:
        cnt += 1
if cnt == len(S):
    print('Yes')
else:
    print('No')
