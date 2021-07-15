n, x = list(map(int, input().split()))

k, b = 1 << n, []
if x >= k:
    print(k - 1)
    b = list(range(1, k))
else:
    print((k - 2) >> 1)
    _b, b = set(range(1, k)), set()
    for bi in _b:
        b.add(bi)
        if x ^ bi in b:
            b.remove(x ^ bi)
    if x in b:
        b.remove(x)

if b:
    b = list(b)
    a = [b[0]] + [b[i] ^ b[i + 1] for i in range(len(b) - 1)]
    print(*a)

