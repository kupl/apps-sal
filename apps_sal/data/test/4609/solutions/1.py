import collections
n = int(input())
arr = [int(input()) for _ in range(n)]
c = collections.Counter(arr)
ans = 0
for v in c.values():
    if v % 2:
        ans += 1
print(ans)
