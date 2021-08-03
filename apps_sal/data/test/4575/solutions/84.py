N = int(input())
D, X = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(int(input()))

total = 0
for i in range(N):
    d = (D - 1) // A[i] + 1
    total += d

print((total + X))
