n = int(input())
ss = [0] * (n + 1)
gg = [0] * (n + 1)
#mins = [0] * n
maxs = [0] * n

curMin = -10 ** 10
curMax = -curMin

for i in range(n):
    s, g = list(map(int, input().split(' ')))
    ss[i] = s
    gg[i] = g

    curMin = max(curMin - 1, s)
    curMax = min(curMax + 1, s + g)
    if curMin > curMax:
        print(-1)
        return
    
    #mins[i] = curMin
    maxs[i] = curMax

res = [0] * n
cur = 10 ** 10
for i in range(n - 1, -1, -1):
    res[i] = cur = min(cur + 1, maxs[i])

print(sum(res) - sum(ss))
print(*res)

