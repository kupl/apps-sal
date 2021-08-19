(X, Y) = map(int, input().split())
ans = 0
now = X
while now <= Y:
    ans += 1
    now *= 2
print(ans)
