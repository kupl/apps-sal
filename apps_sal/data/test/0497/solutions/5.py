n = int(input())
A = [int(x) for x in input().split()]
f = A[0]
l = A[-1]

for i in range(n):
    if A[i] != A[-1]:
        break

for j in reversed(list(range(n))):
    if A[j] != A[0]:
        break

print(max(j + 1, n - i) - 1)
