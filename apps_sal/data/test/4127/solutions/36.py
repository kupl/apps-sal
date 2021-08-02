A, B = map(str, input().split())
A = int(A)
C, D = map(int, B.split('.'))
B1 = C * 100 + D
print(int((A * B1) // 100))
