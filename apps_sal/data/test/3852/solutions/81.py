n = int(input())
a = list(map(int, input().split()))
m = 0
for (i, ai) in enumerate(a):
    if abs(ai) >= m:
        m = abs(ai)
        mi = i
ret = [[mi + 1, i + 1] for i in range(n)]
if a[mi] >= 0:
    for i in range(n - 1):
        ret.append([i + 1, i + 2])
else:
    for i in range(n - 2, -1, -1):
        ret.append([i + 2, i + 1])
print(2 * n - 1)
for x in ret:
    print(' '.join(map(str, x)))
