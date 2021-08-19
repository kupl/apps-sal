N = int(input())
S = str(input())
cnt = 0
for i in range(N - 2):
    if S[i] == 'A' and S[i + 1] == 'B' and (S[i + 2] == 'C'):
        cnt += 1
print(cnt)
