n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

num = 0
for k in list(d.keys()):
    tmp = 0
    for j in range(k, k + 6):
        if j in d:
            tmp += d[j]
    num = max(num, tmp)

print(num)


