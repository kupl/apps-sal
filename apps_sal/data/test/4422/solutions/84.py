(N, K) = map(int, input().split())
S = str(input())
L = []
for i in range(N):
    L.append(S[i])
    if i == K - 1:
        L[i] = S[i].lower()
print(''.join(map(str, L)))
