import collections
n = int(input())
a = list(map(int, input().split()))
l = list(set(a))
m = collections.Counter(a)
ans = 0
for i in range(len(l)):
    if m[l[i]] < l[i]:
        ans += m[l[i]]
    else:
        ans += m[l[i]] - l[i]
print(ans)
