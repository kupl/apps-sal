import collections
l = list(map(int, input().split()))
c = collections.Counter(l)
ans = 'No'

if len(c) == 2:
    ans = 'Yes'
print(ans)
