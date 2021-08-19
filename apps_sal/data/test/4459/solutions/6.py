import collections
N = int(input())
*A, = map(int, input().split())

c = collections.Counter(A)

ans = 0
for k, v in c.items():
    if k == v:
        continue
    if k < v:  # kに対して要素数が多いので取り除く
        ans += v - k
    if v < k:  # kに対して要素数が少ないので、すべて取り除く
        ans += v
print(ans)
