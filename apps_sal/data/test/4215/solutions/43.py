(A, B) = map(int, input().split())
C = A - B * 2
C = 0 if C < 0 else C
print(C)
