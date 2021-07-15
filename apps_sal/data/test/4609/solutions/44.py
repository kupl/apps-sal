n = int(input())
A = {}
for i in range(n):
    a = int(input())
    A[a] = A.get(a, 0)+1
    A[a] %= 2
s = 0
for v in list(A.values()):
    s += v
print(s)

