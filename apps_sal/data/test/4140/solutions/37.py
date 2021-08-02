S = list(input())

cnt = 0

for i in range(len(S) - 1):
    if S[i] == S[i + 1] == '0':
        S[i + 1] = '1'
        cnt += 1
    elif S[i] == S[i + 1] == '1':
        S[i + 1] = '0'
        cnt += 1
    else:
        pass

print(cnt)
