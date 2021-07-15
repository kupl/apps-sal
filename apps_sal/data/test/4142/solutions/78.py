S = input()
cnt = 0
for i in range(0, len(S)):
    if 'L' in S[0::2]:
        cnt += 1
    elif 'R' in S[1::2]:
        cnt += 1
if cnt == 0:
    print('Yes')
else:
    print('No')
