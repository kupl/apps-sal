n, k1, k2 = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = sorted([abs(a[i] - b[i]) for i in range(n)])[::-1]
k = k1 + k2
cur = 0
for i in range(k):
    if c[0] == 0:
        break
    cur += 1
    c[0] -= 1
    j = 0
    while j + 1 < n and c[j] < c[j + 1]:
        c[j], c[j + 1] = c[j + 1], c[j]
        j += 1
k -= cur
if k > 0:
    print(k % 2)
else:
    ans = 0
    for i in c:
        ans += i**2
    print(ans)
