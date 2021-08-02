S = input()
T = [0] * len(S)
A = [0] * (len(S) - 2)

for i in range(len(S)):
    T[i] = int(S[i])

for j in range(len(S) - 2):
    A[j] = 100 * T[j] + 10 * T[j + 1] + T[j + 2]
    A[j] = abs(A[j] - 753)

print((min(A)))
