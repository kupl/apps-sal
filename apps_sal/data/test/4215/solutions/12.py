A, B = map(int, input().split())
X = A - B * 2
if X < 0:
    print(0)
else:
    print(X)
