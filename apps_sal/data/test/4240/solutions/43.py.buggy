S = input()
T = input()
N = len(S)
for i in range(N - 1, -1, -1):
    if S[:i] == T[N - i:] and S[i:] == T[:N - i]:
        print('Yes')
        return
print('No')
