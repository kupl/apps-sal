import math
n = int(input())
p = list(map(int, input().split()))
c = 0
s = []
for i in range(n):
    if p[i] == i + 1:
        c += 1
    elif c > 0:
        s.append(c)
        c = 0
if c > 0:
    s.append(c)
ans = 0
for i in s:
    if i == 1:
        ans += 1
    else:
        ans += math.ceil(i / 2)
print(ans)
