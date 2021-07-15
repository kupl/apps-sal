n = int(input())
d = {}
a = list(map(int, input().split()))
for i in range(n):
    if a[i] not in d:
        d[a[i]] = (1, n - i)
    else:
        d[a[i]] = (d[a[i]][0] + 1, n - i)
print(sorted(d.items(), key = lambda x: x[1])[-1][0])
