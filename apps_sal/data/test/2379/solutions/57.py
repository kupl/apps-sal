(N, K, C) = map(int, input().split())
S = list(input())
A = [0] * N
B = [0] * N
i = 0
a = 1
while i < N:
    if S[i] == 'o':
        A[i] = a
        a += 1
        i += C + 1
    else:
        i += 1
j = N - 1
b = K
while j >= 0:
    if S[j] == 'o':
        B[j] = b
        b -= 1
        j -= C + 1
    else:
        j -= 1
for i in range(N):
    if A[i] == B[i] and A[i] != 0:
        print(i + 1)
