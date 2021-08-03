import collections

n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)
ans = 0

for k, v in list(c.items()):
    if k > v:
        ans += v
    if k < v:
        ans += v - k

print(ans)
