import collections
n = int(input())
l = list((int(input()) for i in range(n)))
d = collections.Counter(l)
ans = 0
for v in d.values():
    ans += v % 2
print(ans)
