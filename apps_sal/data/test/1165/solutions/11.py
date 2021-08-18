
n, m = tuple(map(int, input().split()))
li = input().split()
a = [0] * n
for i in range(1, n):
    if li[i] != li[i - 1]:
        a[i] = (i)
    else:
        a[i] = (a[i - 1])
result = [0] * m
for k in range(m):
    l, r, x = input().split()
    l, r = int(l), int(r)
    if li[r - 1] != x:
        result[k] = str(r)
    elif a[r - 1] >= l:
        result[k] = str(a[r - 1])
    else:
        result[k] = '-1'

print('\n'.join(result))
