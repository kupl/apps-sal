(n, m, k) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a = a[::-1]
boxes = 0
ans = 0
loc = 0
for i in range(n):
    loc += a[i]
    if loc > k:
        boxes += 1
        loc = a[i]
    if boxes == m:
        break
    ans += 1
print(ans)
