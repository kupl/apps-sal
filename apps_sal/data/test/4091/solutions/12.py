(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
b = b[:k]
s = sum(b)
rec = []
k = 1
for i in range(n):
    if a[i] not in b:
        k += 1
        continue
    else:
        b.remove(a[i])
        rec.append(k)
        k = 1
rec[-1] += n - sum(rec)
print(s)
print(' '.join(map(str, rec)))
