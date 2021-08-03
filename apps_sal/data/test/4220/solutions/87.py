K = int(input())
S = input()
N = len(S)

if N <= K:
    print(S)
else:
    ans = []
    for i in range(K):
        ans.append(S[i])
    print(''.join(ans) + '...')
