def I():
    return list(map(int, input().split()))


(n, k) = I()
a = sorted(I())
b = set(a)
if k != 1:
    for i in a:
        if i in b:
            b.discard(i * k)
print(len(b))
