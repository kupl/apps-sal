def check(x):
    last = [0] * (n + 1)
    for i in tmp:
        if i[0] > x:
            break
        else:
            last[i[1]] = i[0]
    sal = [0] * (x + 1)
    for i in range(1, n + 1):
        sal[last[i]] += lis[i - 1]
    c = 0
    for i in range(1, x + 1):
        c += 1
        if sal[i] >= c:
            sal[i] -= c
            c = 0
        else:
            c -= sal[i]
            sal[i] = 0
    if sum(sal) * 2 <= c:
        return True
    else:
        return False


(n, m) = list(map(int, input().split()))
lis = list(map(int, input().split()))
tmp = []
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    tmp.append([a, b])
tmp.sort()
l = 0
r = sum(lis) * 2
while l <= r:
    mid = l + (r - l) // 2
    if check(mid):
        r = mid - 1
    else:
        l = mid + 1
if check(r):
    print(r)
elif check(l):
    print(l)
else:
    print(l + 1)
