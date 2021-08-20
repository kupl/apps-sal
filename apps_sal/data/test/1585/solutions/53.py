(X, Y) = map(int, input().split())
cnt = 0
A = X
while A <= Y:
    A = A * 2
    cnt += 1
print(cnt)
