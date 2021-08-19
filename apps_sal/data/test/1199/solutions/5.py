def takefirst(eml):
    return eml[0]


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = []
a.append(0)
max1 = 0
c = 0
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        c += 1
        max1 = max(max1, c)
        c = 0
    else:
        c += 1
a.pop()
ans = []
total = 0
for i in range(len(a)):
    ans.append((a[i], a[(i + max1) % len(a)]))
    if a[i] != a[(i + max1) % len(a)]:
        total += 1
print(total)
for i in range(len(ans)):
    print('{0} {1}'.format(ans[i][0], ans[i][1]))
