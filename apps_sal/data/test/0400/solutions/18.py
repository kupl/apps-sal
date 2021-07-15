from copy import deepcopy
n, k = map(int, input().split())
l = list(map(int, input().split()))
k1 = deepcopy(l)
ans = 0
v = 0
l = deepcopy(k1)
for i in range(n):
    l[i] = [l[i], i]
for i in range(n):
    if l[i][0] == 100:
        l[i][0] = -1
        k1[i] = -1
    else:
        l[i][0] %= 10
cur = 10**9
l.sort(reverse = True)
for i in range(n):
    if l[i][0] >= 0:
        cur = 10 - (l[i][0] % 10)
        if k < cur:
            break
        else:
            k -= cur
            k1[l[i][1]] += cur
g = 0
for i in range(n):
    if k1[i] >= 0:
        g += 10 - k1[i] // 10

for i in range(n):
    if k1[i] >= 0:
        ans += k1[i] // 10
    else:
        ans += 10
    
print(ans + min(g, k // 10))
