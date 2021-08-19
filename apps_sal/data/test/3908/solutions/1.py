A = [ord(a) - 97 for a in input()]
N = len(A)
X = [0] * 26
Y = [[0] * 26 for _ in range(26)]
for a in A:
    for k in range(26):
        Y[k][a] += X[k]
    X[a] += 1
print(max([max(y) for y in Y] + X))
