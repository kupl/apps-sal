S = str(input())
N = len(S)
cnt = 0
for i in range(N):
    if S[0] == '0':
        if i % 2 == 0 and S[i] != '0':
            cnt += 1
        elif i % 2 == 1 and S[i] == '0':
            cnt += 1
    elif i % 2 == 0 and S[i] != '1':
        cnt += 1
    elif i % 2 == 1 and S[i] == '1':
        cnt += 1
print(cnt)
