S = str(input())

N = len(S)
cnt = [0 for i in range(N)]
for i in range(N):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
        cnt[i] += 1
        for j in range(i + 1, N):
            if S[j] == 'A' or S[j] == 'C' or S[j] == 'G' or S[j] == 'T':
                cnt[i] += 1
            else:
                break
print(max(cnt))
