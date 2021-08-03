n, k = list(map(int, input().split()))
a = sorted(set(map(int, input().split())))
cur = 0
l = len(a)
for i in range(k):
    if i < l:
        print(a[i] - cur)
        cur = a[i]
    else:
        print(0)
