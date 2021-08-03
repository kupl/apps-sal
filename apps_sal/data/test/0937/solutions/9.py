def R(): return list(map(int, input().split()))


n, k = R()
a = R()
t = R()

g = 0
for i in range(n):
    if t[i]:
        g += a[i]

l = 0
for i in range(0, k):
    if t[i] == 0:
        l += a[i]

max_l = l
for i in range(k, n):
    a_new = a_old = 0
    if t[i - k] == 0:
        a_old = a[i - k]
    if t[i] == 0:
        a_new = a[i]
    l += a_new - a_old
    max_l = max(max_l, l)

print(g + max_l)
