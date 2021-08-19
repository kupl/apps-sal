n = int(input())
A = list(map(int, input().split()))
X = [0] * (10 ** 5 + 5)
for a in A:
    X[a] += 1
    X[a + 1] += 1
    X[a - 1] += 1
print(max(X))
