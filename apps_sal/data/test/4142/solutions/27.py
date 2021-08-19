S = input()
cnt = 0
for i in range(0, len(S)):
    if i % 2 == 0:  # 奇数文字目
        if S[i] in ['R', 'U', 'D']:
            cnt += 1
    else:  # 偶数文字目
        if S[i] in ['L', 'U', 'D']:
            cnt += 1
if cnt == len(S):
    print('Yes')
else:
    print('No')
