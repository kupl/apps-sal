n = int(input())
A = list(map(int, input().split()))
s = 0
for i in range(n):
    s += 1 / A[i]
print((1 / s))
