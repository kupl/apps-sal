(e1, e2, e3) = map(int, input().split())
A = e1 + e2
B = e2 + e3
C = e1 + e3
print(min(A, B, C))
