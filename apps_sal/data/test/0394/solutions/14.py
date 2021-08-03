n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
l = []
for i in range(n):
    l.append(a[i + 1] - a[i])
r = []
for i in range(1, n + 1):
    m = l[:i]
    j = 0
    k = i
    f = True
    while k < n:
        if m[j] == l[k]:
            j = (j + 1) % i
            k += 1
        else:
            f = False
            break
    if f == True:
        r.append(i)
print(len(r))
print(' '.join(map(str, r)))
