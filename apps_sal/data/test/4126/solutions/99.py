S = input()
N = len(S)
S_f = S[:int((N-1)/2)]
S_b = S[int((N+1)/2):]
a = []
for i in range(int(len(S)/2)):
    if S[i] == S[len(S)-i-1]:
        a.append(0)
    else:
        a.append(1)
for i in range (int(len(S_f)/2)):
    if S_f[i] == S_f[len(S_f)-i-1]:
        a.append(0)
    else:
        a.append(1)
for i in range (int(len(S_b)/2)):
    if S_b[i] == S_b[len(S_b)-i-1]:
        a.append(0)
    else:
        a.append(1)
if sum(a) == 0:
    print('Yes')
else:
    print('No')
