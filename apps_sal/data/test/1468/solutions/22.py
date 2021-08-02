n = int(input())
a = [input() for i in range(n)]
for i in range(n - 1, 0, -1):
    b = a[i]
    c = a[i - 1]
    l1 = len(b)
    l2 = len(c)
    for j in range(min(l1, l2)):
        if b[j] < c[j]:
            a[i - 1] = c[:j]
            break
        elif b[j] > c[j]:
            break
    else:
        if l2 > l1:
            a[i - 1] = a[i]
print('\n'.join(a))
