n, s = [int(i) for i in input().split()]
ll = [int(i) for i in input().split()]
curr = 0
l = 0
h = n
while l <= h:
    mid = (h + l) // 2
    k = ll[:]
    for i in range(n):
        k[i] = (i + 1) * mid + ll[i]
    k.sort()
    sm = sum(k[:mid])
    if sm <= s:
        curr = mid
        l = mid + 1
        ans = sm
    else:
        h = mid - 1
print(curr, ans)
