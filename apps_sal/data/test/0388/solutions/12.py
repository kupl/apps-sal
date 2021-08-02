n, k = list(map(int, input().split()))
a = input().split()
uq_names = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
uq_names += [s + 'a' for s in uq_names]
res = uq_names[:k - 1]
uni = k - 1
for i, b in enumerate(a):
    if b == "YES":
        res.append(uq_names[uni])
        uni += 1
    else:
        res.append(res[i])
print(' '.join(res))
