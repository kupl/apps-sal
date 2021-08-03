import math
s = input().split()
n, l = int(s[0]), int(s[1])
a = input().split()
a = [int(a) for a in a]
a.sort()
ans = max(a[0], l - a[n - 1])
for i in range(n - 1):
    ans = max(ans, (a[i + 1] - a[i]) / 2)
print('%.9f' % ans)
