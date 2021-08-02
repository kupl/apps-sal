n, l = list(map(int, input().split()))

apples = []
ans = 300
for i in range(1, n + 1):
    taste = i + l - 1
    apples.append(taste)
    if abs(taste) < abs(ans):
        ans = taste

apples.remove(ans)
print((sum(apples)))
