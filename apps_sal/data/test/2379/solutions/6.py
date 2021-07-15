N, K, C = list(map(int, input().split()))
S = input()

F = {}
i = 0
c = 1
while i < N and c <= K:
    if S[i] == 'x':
        i += 1
        continue
    F[c] = i + 1
    i += C + 1
    c += 1

L = {}
i = N - 1
c = K
while i >= 0 and c >= 1:
    if S[i] == 'x':
        i -= 1
        continue
    L[c] = i + 1
    i -= C + 1
    c -= 1

for i in range(1, K + 1):
    if F[i] == L[i]:
        print((F[i]))

