S = input()
T = input()
R = len(S)
A = 0
for k in range(R):
    if S[k - 1] != T[k - 1]:
        A += 1
print(A)
