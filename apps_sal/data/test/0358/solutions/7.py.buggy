p = [1] * (1000005)
p[0] = 0
p[1] = 0
for i in range(2, 1001):
    if p[i]:
        for j in range(2 * i, 1000005, i):
            p[j] = 0
for i in range(1, 1000001):
    p[i] += p[i - 1]
a, b, k = map(int, input().split())
if p[b] - p[a - 1] < k:
    print(-1)
    return()
i = j = a
l = 0
while j <= b:
    if p[j] - p[i - 1] < k:
        j += 1
    else:
        l = max(l, j - i + 1)
        i += 1
l = max(j - i + 1, l)
print(l)
