(n, k) = [int(c) for c in input().split()]
ar = []
while n != 0:
    ar.append(n % 10)
    n = n // 10
ar.reverse()
i = 0
while k > 0 and i < len(ar):
    m_val = max(ar[i:i + k + 1])
    pos = i
    while ar[pos] != m_val:
        pos += 1
    while pos != i:
        (ar[pos], ar[pos - 1]) = (ar[pos - 1], ar[pos])
        pos -= 1
        k -= 1
    i += 1
print(''.join(map(str, ar)))
