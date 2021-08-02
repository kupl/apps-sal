# bismillah
n, m = list(map(int, input().split()))
a = list(map(int, input().split(' ')))
o = 0; c = 0; t = []; sm = n
for i in range(m + 1):
    t.append(0)
for i in range(n):
    t[a[i]] += 1
for i in range(1, m + 1):
    sm -= t[i]
    o += t[i] * sm
print(o)
