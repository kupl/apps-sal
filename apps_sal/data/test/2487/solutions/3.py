n = int(input())
ans = int(n * (n + 1) * (n + 2) / 6)
for i in range(n - 1):
    (x, y) = map(int, input().split(' '))
    ans -= y * (n + 1 - x) if x > y else x * (n + 1 - y)
print(ans)
