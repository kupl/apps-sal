S = input()
T = input()
cnt = 0
for i in range(len(S)):
    S = S[-1] + S[0:-1]
    if S == T:
        cnt = 1
        print('Yes')
        break
if cnt == 0:
    print('No')
