(p, k) = list(map(int, input().split(' ')))
a = []
while p:
    a.append(p % k)
    p = -(p // k)
print(len(a))
print(' '.join((str(a[i]) for i in range(len(a)))))
