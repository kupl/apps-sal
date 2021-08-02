n = int(input())
a = [int(x) for x in input().split()]

l = []
if n % 2 == 1:
    i = n - 1
    while i >= 0:
        l.append(a[i])
        i -= 2

    j = 1
    while j < n:
        l.append(a[j])
        j += 2
else:
    i = n - 1
    while i >= 0:
        l.append(a[i])
        i -= 2

    j = 0
    while j < n:
        l.append(a[j])
        j += 2

print((' '.join(map(str, l))))
