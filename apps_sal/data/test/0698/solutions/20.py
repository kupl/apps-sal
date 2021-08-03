x, k = [int(x) for x in input().split()]
used = [0, x]
for i in range(k):
    a, *l = [int(x) for x in input().split()]
    used += l
used.sort()
m = M = 0
for i in range(len(used) - 1):
    M += used[i + 1] - used[i] - 1
    m += (used[i + 1] - used[i]) // 2
print(m, M)
