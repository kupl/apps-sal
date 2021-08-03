S = input()

cnt = 0
for i in range(int(len(S) / 2)):
    if S[i] == S[len(S) - 1 - i]:
        continue
    else:
        cnt += 1
        #print(i, S[i], S[len(S)-1-i])
print(cnt)
