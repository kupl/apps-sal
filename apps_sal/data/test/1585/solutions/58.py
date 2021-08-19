(X, Y) = map(int, input().split())
cnt = 0
a = X
while a <= Y:
    cnt += 1
    a *= 2
print(cnt)
