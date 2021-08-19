import sys
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
(N, K, C) = map(int, input().split())
S = list(input())
mae = [-1] * N
i = 0
count = 0
while i < N and count < K:
    if S[i] == 'o':
        mae[i] = count
        count += 1
        i += C + 1
    else:
        i += 1
ushiro = [-1] * N
i = N - 1
count = 0
while i >= 0 and count < K:
    if S[i] == 'o':
        ushiro[i] = K - count - 1
        count += 1
        i -= C + 1
    else:
        i -= 1
for i in range(N):
    if mae[i] == ushiro[i] and mae[i] != -1:
        print(i + 1)
