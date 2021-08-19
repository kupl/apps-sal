N = int(input())
a = []
b = []
for i in range(N):
    (x, y) = map(int, input().split())
    a.append(x + y)
    b.append(x - y)
A = max(a) - min(a)
B = max(b) - min(b)
print(max(A, B))
