(a, b, c) = map(int, input().split())
A = a + b
B = b + c
C = c + a
print(min(A, B, C))
