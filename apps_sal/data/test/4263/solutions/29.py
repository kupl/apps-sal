S = input()
cnt = 0
maxv = 0
for i in range(len(S)):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or (S[i] == 'T'):
        cnt += 1
        if cnt > maxv:
            maxv = cnt
    else:
        cnt = 0
print(maxv)
