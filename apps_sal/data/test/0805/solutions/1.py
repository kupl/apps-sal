n = int(input())
l = []
r = []
for i in range(0, n):
    a = list(map(int, input().split()))
    l.append(a[0])
    r.append(a[1])
ans = 0
for j in range(l[0], r[0]):
    for k in range(1, n):
        if j < r[k] and j >= l[k]:
            break
    else:
        ans += 1
print(str(ans))
