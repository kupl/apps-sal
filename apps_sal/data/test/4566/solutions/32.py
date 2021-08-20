(n, m) = map(int, input().split())
A = []
B = []
for i in range(m):
    (a, b) = map(int, input().split())
    A.append(a)
    B.append(b)
for j in range(n):
    print(A.count(j + 1) + B.count(j + 1))
