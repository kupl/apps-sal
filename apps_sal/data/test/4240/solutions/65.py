S = input()
T = input()
S_len = len(S)
S_change = ''
answer = 'No'
for _ in range(0, S_len):
    if S == T:
        answer = 'Yes'
        break
    S_change = S[-1]
    S = S[:-1]
    S = S_change + S
print(answer)
