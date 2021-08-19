import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = 0
for i in c.keys():
    if c[i] >= i:
        ans += c[i] - i
    else:
        ans += c[i]
print(ans)
