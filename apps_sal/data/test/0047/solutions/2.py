n, x = map(int, input().split())
l = list(map(int, input().split()))
not_used = [0 for k in range(n + 1)]
current = [0 for k in range(n + 1)]
used = [0 for k in range(n + 1)]
globalMax = 0
for k in range(n):
    not_used[k + 1] = max(not_used[k], 0) + l[k]
    current[k + 1] = max(max(not_used[k], current[k]), 0) + l[k] * x
    used[k + 1] = max(max(current[k], used[k]), 0) + l[k]
    globalMax = max(max(globalMax, used[k + 1]), max(current[k + 1], not_used[k + 1]))
print(globalMax)
