S = input()
K = int(input())
A = []
for i in range(len(S)):
    for j in range(1, 6):
        a = S[i:i + j]
        A.append(a)
        # print(A)

A = set(A)
A = sorted(set(A))
print(A[K - 1])
