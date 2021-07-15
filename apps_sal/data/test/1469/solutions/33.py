L = int(input())
N = L.bit_length()

res = []

for i in range(N - 1):
    res.append((i + 1, i + 2, 1 << i))
    res.append((i + 1, i + 2, 0))

n = 1 << (i + 1)
m = L - n

for i in reversed(range(m.bit_length())):
    if (m >> i) & 1:
        m %= (1 << i)
        res.append((i + 1, N, n))
        n += (1 << i)


print(N, len(res))

for i in range(len(res)):
    print(*res[i])
