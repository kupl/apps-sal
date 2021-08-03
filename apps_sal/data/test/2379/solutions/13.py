N, K, C = list(map(int, input().split()))
S = input()

l = [-1] * N
r = [-1] * N

idx = 1
i = 0
C += 1

while i < N:
    if S[i] == 'o':
        l[i] = idx
        idx += 1
        i += C
    else:
        i += 1

idx = 1
i = N - 1
while 0 <= i:
    if S[i] == 'o':
        r[i] = idx
        idx += 1
        i -= C
    else:
        i -= 1

if idx - 1 <= K:
    for i in range(N):
        if l[i] != -1 and r[i] != -1:
            print(i + 1)
