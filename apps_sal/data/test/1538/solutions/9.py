import sys
p = {}
n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    if a[i] not in p:
        p[a[i]] = 1
    else:
        p[a[i]] += 1
    ans = max(ans, p[a[i]])
print(ans)
