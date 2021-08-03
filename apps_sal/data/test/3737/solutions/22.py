i = int(input())
A = list(map(int, input().split()))

A = sorted(A)
a_min = A[0]
a_max = A[len(A) - 1]
B = []

for i in range(1, len(A) - 1):
    if A[i] != a_min and A[i] != a_max:
        B.append(A[i])

print(len(B))
