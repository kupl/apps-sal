S = input()
T = input()
N = len(S)

for i in range(N):
    if S[i] != T[i]:
        print('No')
        return
print('Yes')
