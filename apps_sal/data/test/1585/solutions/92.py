X, Y = list(map(int, input().split()))

ans = 1
tmp = X
while tmp*2 <= Y:
    ans += 1
    tmp *= 2
print(ans)

