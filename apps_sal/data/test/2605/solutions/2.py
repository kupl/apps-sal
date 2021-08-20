(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = set(map(int, input().split()))
t = 0
p = 0
q = 0
s = 0
for (i, x) in enumerate(a):
    if i + 1 in b:
        t += x * s
        p += x - q
        q = 0
    else:
        t += x * p
        p += x - q
        q = x
    s += x
if n not in b and 1 not in b:
    t += a[-1] * a[0]
print(t)
