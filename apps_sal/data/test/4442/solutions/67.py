a, b = map(int, input().split())

A = str(a) * int(b)
B = str(b) * int(a)
print(min(A, B))
