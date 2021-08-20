(N, K) = map(int, input().split())
S = list(input())
tmp = []
tmp.append(S[0])
for i in range(1, N):
    if S[i] != S[i - 1]:
        tmp.append(S[i])
G = len(tmp)
G -= 2 * K
G = max(G - 1, 0)
print(N - G - 1)
