(X, Y) = map(int, input().split())
cnt = 0
while X <= Y:
    X *= 2
    cnt += 1
print(cnt)
