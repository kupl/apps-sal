N = int(input())
A = [int(a) for a in input()]
X = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    X.append((a, b))
ma = sum(A)
for i in range(151):
    for j in range(N):
        if i >= X[j][1] and (i - X[j][1]) % X[j][0] == 0:
            A[j] ^= 1
    ma = max(ma, sum(A))

print(ma)
