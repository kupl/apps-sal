(n, k) = map(int, input().split())
bits = [0 for i in range(128)]
tmp = n
sumBits = 0
for i in range(64):
    if tmp % 2 == 1:
        bits[63 - i] = 1
        sumBits += 1
    tmp = tmp >> 1
if sumBits > k:
    print('No')
elif sumBits == k:
    print('Yes')
    res = []
    for i in range(63, -1, -1):
        if bits[63 - i] == 1:
            res.append(i)
    print(*res)
else:
    ind = 0
    while k != sumBits:
        if bits[ind] != 0:
            if bits[ind] <= k - sumBits:
                bits[ind + 1] += 2 * bits[ind]
                sumBits += bits[ind]
                bits[ind] = 0
            else:
                break
        ind += 1
    if k != sumBits:
        for i in range(127, -1, -1):
            if bits[i] != 0:
                bits[i] -= 1
                first = i + 1
                break
        if k - sumBits < 128 - first:
            for i in range(first, k - sumBits + first):
                bits[i] = 1
            bits[k - sumBits + first - 1] = 2
        else:
            for i in range(first, 128):
                bits[i] = 1
            bits += [1] * (k - sumBits + first - 128)
            bits[-1] = 2
    print('Yes')
    res = []
    for i in range(len(bits)):
        if bits[i] != 0:
            res += [63 - i] * bits[i]
    print(*res)
