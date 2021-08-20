S = input()
T = input()
N = len(S)
for i in range(N + 1):
    if S[-i:N] + S[0:-i + N] == T:
        print('Yes')
        break
else:
    print('No')
