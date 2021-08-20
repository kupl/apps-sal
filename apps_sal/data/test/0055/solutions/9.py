from collections import Counter
bits = (10 ** 18).bit_length()
(n, k) = map(int, input().split())
num = Counter((i for i in range(bits) if n >> i & 1))
k -= len(num)
if k >= 0:
    print('Yes')
    for i in range(bits, -bits, -1):
        if num[i] > k:
            break
        num[i - 1] += num[i] * 2
        k -= num.pop(i, 0)
    i = next(filter(num.get, range(-bits, bits)))
    for k in range(k):
        num[i] -= 1
        num[i - 1] += 2
        i -= 1
    s = sorted(num.elements(), reverse=True)
    print(' '.join(map(str, s)))
else:
    print('No')
