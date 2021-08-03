(n, p, q, r2) = list(map(int, input().split()))
a = list(map(int, input().split()))
# print(a);
# print(p);
small = 10**9 + 1
large = -10**9 - 1
infa = 10**9 + 1
infb = -10**9 - 1
l = []
r = []
for i in range(0, n):
    small = min(small, a[i])
    large = max(large, a[i])
    l.append((small, large))
small = 10**9 + 1
large = -10**9 - 1
for i in range(n - 1, -1, -1):
    small = min(small, a[i])
    large = max(large, a[i])
    r.append((small, large))
r = r[-1::-1]
# print(l);
# print(r);
s = 0
x = a[0]
maxs = x * p + x * q + x * r2
for i in range(n):
    s = 0
    if(p > 0):
        s = s + p * l[i][1]
    else:
        s = s + p * l[i][0]
    if(r2 > 0):
        s = s + r2 * r[i][1]
    else:
        s = s + r2 * r[i][0]
    s = s + q * a[i]
    # print(s);

    maxs = max(s, maxs)
print(maxs)
