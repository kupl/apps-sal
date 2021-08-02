K = int(input())
X = 50

A = [X - 1] * X
A = [a + K // X for a in A]
for i in range(K % X):
    A[i] += 1
for i in range(X - (K % X)):
    A[-i - 1] -= K % X

print(X)
print(*A, sep=' ')
