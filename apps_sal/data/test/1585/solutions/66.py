(x, y) = map(int, input().split())
n = x
ans = 0
while n <= y:
    n *= 2
    ans += 1
print(ans)
