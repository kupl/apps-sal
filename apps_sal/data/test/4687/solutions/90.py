(n, k) = list(map(int, input().split()))
ar = {}
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if (a in ar) == True:
        ar[a] += b
    else:
        ar[a] = b
for i in sorted(ar.keys()):
    k -= ar[i]
    if k <= 0:
        print(i)
        break
