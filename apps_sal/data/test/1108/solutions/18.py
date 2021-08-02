n = int(input())
ans = 0
for i in range(n):
    x, y = [int(x) for x in input().split()]
    if y - x >= 2:
        ans += 1
print(ans)
