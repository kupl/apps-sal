T = input().split(' ')
n = int(T[0])
k = int(T[1])
S = input().split(' ')
for i in range(len(S)):
    S[i] = (int(S[i]), i)
Q = S.copy()
S.sort()
N = [0] * len(S)
tot = 0
for i in range(1, len(S)):
    if S[i][0] == S[i - 1][0]:
        tot += 1
    else:
        tot = 0
    N[S[i][1]] = i - tot
B = [0] * len(S)
for i in range(k):
    W = input().split(' ')
    a = int(W[0])
    b = int(W[1])
    if Q[a - 1][0] > Q[b - 1][0]:
        B[a - 1] += 1
    if Q[b - 1][0] > Q[a - 1][0]:
        B[b - 1] += 1
for i in range(len(S) - 1):
    print(N[i] - B[i], end=' ')
print(N[n - 1] - B[n - 1])
