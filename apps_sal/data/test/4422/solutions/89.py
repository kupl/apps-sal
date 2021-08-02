N, K = map(int, input().split())
S = list(input())
for i in range(N):
    if i == K - 1:
        S[i] = chr(ord(S[i]) + 32)
print(''.join(S))
