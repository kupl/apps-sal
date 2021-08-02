N = int(input())
A = [int(i) for i in input().split()]
s = 0
for i in range(N):
    s += 1 / A[i]
print(1 / s)
