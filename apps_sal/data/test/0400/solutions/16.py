n, k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
assert len(l) == n
assert all(0 <= x <= 100 for x in l)
f = [10-l[i]%10 for i in range(n) if l[i]%10]
f.sort()
cur = sum(x // 10 for x in l)
for x in f:
    if k >= x:
        cur += 1
        k -= x
print(min(cur + k // 10, 10 * n))
#print(cur + k // 10)

