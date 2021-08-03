n = int(input())
index6, index9, num6, num9 = 0, 0, 0, 0
INF = float('inf')
a = [INF for _ in range(n + 1)]
a[n] = 0

for i in range(n, -1, -1):
    if a[i] == INF:
        continue
    j = 1
    while i - 9**j >= 0:
        a[i - 9**j] = min(a[i] + 1, a[i - 9**j])
        j += 1
    j = 1
    while i - 6**j >= 0:
        a[i - 6**j] = min(a[i] + 1, a[i - 6**j])
        j += 1
    if i - 1 >= 0:
        a[i - 1] = min(a[i] + 1, a[i - 1])
print((a[0]))
