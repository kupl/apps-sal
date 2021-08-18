import collections
N = int(input())
*A, = map(int, input().split())

c = collections.Counter(A)

ans = 0
for k, v in c.items():
    if k == v:
        continue
    if k < v:
        ans += v - k
    if v < k:
        ans += v
print(ans)
