n, k = list(map(int, input().split()))
a = sorted(list(set(map(int, input().split()))))
if 0 in a:
    a.remove(0)
q1 = 0
for q in range(k):
    if q < len(a):
        print(a[q]-q1)
        q1 += a[q]-q1
    else:
        print(0)

