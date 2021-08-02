N = int(input())
S = sorted([input() for _ in range(N)])
A = []
count = 1
for i in range(N - 1):
    if(i == N - 2):
        A.append(S[N - 1])
    if(S[i] != S[i + 1]):
        A.append(S[i])
A.sort()
B = [1] * len(A)
a = 0
for i in range(N - 1):
    if(S[i] == S[i + 1]):
        B[a] += 1
    else:
        a += 1
m = max(B)
for i in range(len(A)):
    if(B[i] == m):
        print(A[i])
