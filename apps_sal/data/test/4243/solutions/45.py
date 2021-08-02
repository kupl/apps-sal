X = int(input())
C = X // 500
c = (X - X // 500 * 500) // 5
print(C * 1000 + c * 5)
