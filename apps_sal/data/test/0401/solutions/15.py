n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
am = min(a)
bm = min(b)
mi = 100
for i in range(n):
    if a[i] in b and a[i] < mi:
        mi = a[i]
if mi < 10:
    print(mi)

elif am == bm:
    print(am)
else:
    print(10 * min(am, bm) + max(am, bm))
