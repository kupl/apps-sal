n = int(input())
S = [input().strip() for _ in range(n)]
C = {chr(i): 0 for i in range(97, 123)}
for i in range(len(S[0])):
    C[S[0][i]] += 1
for j in range(1, n):
    C1 = {chr(i): 0 for i in range(97, 123)}
    for i in range(len(S[j])):
        C1[S[j][i]] += 1
    for i in range(97, 123):
        C[chr(i)] = min(C[chr(i)], C1[chr(i)])

A = []
for i in range(97, 123):
    A.append(chr(i) * C[chr(i)])
print("".join(sorted(A)))
