#Python is love <3
n, k = map(int, input().split())
a = list(map(int, input().split()))
fix = -1
maxi = -1
box = -1
for i in range(k):
    to = n // a[i]
    tot = to * a[i]
    # print(to,tot)
    if tot > fix:
        fix = tot
        maxi = to
        box = i + 1
print(box, maxi)
