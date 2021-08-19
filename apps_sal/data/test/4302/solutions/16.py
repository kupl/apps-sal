(a, b) = map(int, input().split())
A = a + b
B = a + a - 1
C = b + b - 1
L = [A, B, C]
print(max(L))
