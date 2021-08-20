(X, Y) = map(int, input().split())
n = 0
while 2 ** n * X <= Y:
    n += 1
print(n)
