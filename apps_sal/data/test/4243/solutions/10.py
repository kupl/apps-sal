X = int(input())
Y = X // 500 * 1000
Z = X % 500 // 5 * 5
if X < 500:
    print(X // 5 * 5)
else:
    print(Y + Z)
