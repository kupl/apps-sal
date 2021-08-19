L = int(input())
N = L.bit_length()
res = []
for i in range(N - 1):
    res.append((i + 1, i + 2, 0))
    res.append((i + 1, i + 2, 2 ** i))
rem = L - 2 ** (N - 1)
k = 2 ** (N - 1)
for i in range(rem.bit_length())[::-1]:
    if rem >> i & 1:
        res.append((i + 1, N, k))
        k += 2 ** i
print(N, len(res))
for r in res:
    print(*r)
