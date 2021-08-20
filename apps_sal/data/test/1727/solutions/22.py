n = int(input())
trees = [tuple(map(int, input().split())) for i in range(n)]
prevx = -1000000000000000.0
ans = 0
for i in range(n):
    if i == n - 1:
        ans += 1
        break
    (x, h) = trees[i]
    if x - h > prevx:
        prevx = x
        ans += 1
    elif x + h < trees[i + 1][0]:
        ans += 1
        prevx = x + h
    else:
        prevx = x
print(ans)
