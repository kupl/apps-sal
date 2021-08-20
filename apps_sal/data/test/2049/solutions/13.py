(n, m) = map(int, input().split())
(*a,) = map(int, input().split())
inc = [*range(n)]
dec = [*range(n)]
for i in range(n - 1, 0, -1):
    if a[i] >= a[i - 1]:
        inc[i - 1] = inc[i]
    if a[i] <= a[i - 1]:
        dec[i - 1] = dec[i]
k = ['No'] * m
l = 0
for (i, j) in (map(lambda i: int(i) - 1, input().split()) for _ in ' ' * m):
    if dec[inc[i]] >= j:
        k[l] = 'Yes'
    l += 1
print('\n'.join(k))
