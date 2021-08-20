n = int(input())
a = [int(i) for i in input().split()]
M = max(a)
m = min(a)
ans = []
if m >= 0:
    for i in range(1, n):
        a[i] += a[i - 1]
        ans.append([i, i + 1])
elif M <= 0:
    for i in range(n - 1)[::-1]:
        a[i] += a[i + 1]
        ans.append([i + 2, i + 1])
elif M > -m:
    index = a.index(M)
    for i in range(n):
        if a[i] < 0:
            a[i] += M
            ans.append([index + 1, i + 1])
    for i in range(1, n):
        a[i] += a[i - 1]
        ans.append([i, i + 1])
else:
    index = a.index(m)
    for i in range(n):
        if a[i] > 0:
            a[i] += m
            ans.append([index + 1, i + 1])
    for i in range(n - 1)[::-1]:
        a[i] += a[i + 1]
        ans.append([i + 2, i + 1])
print(len(ans))
print('\n'.join([str(i) + ' ' + str(j) for (i, j) in ans]))
