a, b = map(int, input().split())
A = []
c = 1
for i in range(2, 1001):
    A.append(c)
    c += i
d = b - a
print(A[d - 2] - a)
