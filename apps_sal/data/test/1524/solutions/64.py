S = input()
RL = []
LR = []
N = len(S)
for i in range(N - 1):
    if S[i] == 'R' and S[i + 1] == 'L':
        RL.append(i)
    elif S[i] == 'L' and S[i + 1] == 'R':
        LR.append(i)
LR.append(N)
j = 0
k = 0
cnt = [0 for i in range(N)]
for i in range(N):
    if i > LR[k]:
        j += 1
        k += 1
    if abs(RL[j] - i) % 2 == 0:
        cnt[RL[j]] += 1
    else:
        cnt[RL[j] + 1] += 1
for i in range(N):
    print(cnt[i], end=' ')
print()
