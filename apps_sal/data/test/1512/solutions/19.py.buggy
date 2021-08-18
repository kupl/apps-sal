n = int(input())
m1 = 0
m2 = 0
a = [0] * (n + 1)
a[0] = -n - 5
mini = n + 5
k = list(map(int, input().split()))
m = 0

for i in k:
    if i > m:
        a[i] = -1
    else:
        a[i] = 0
    m = max(m, i)

if n == 1:
    print(k[0])
    return

for i in k:
    mini = min(mini, i)
    if m1 > i > m2:
        a[m1] += 1
        m2 = int(i)
    if i > m1:
        m2 = int(m1)
        m1 = int(i)

m = max(a)
if m == 0:
    print(min(k[1:]))
else:
    print(a.index(m))
