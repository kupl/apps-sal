X, Y = map(int, input().split())
ans = 0
while X <= Y:
    X = 2 * X
    ans += 1
print(ans)
