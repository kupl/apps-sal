L = int(input())


N = L.bit_length()
ans = []
for i in range(N - 1):
    ans.append((i, i + 1, 0))
    ans.append((i, i + 1, 2 ** (N - i - 2)))


X = L - 2 ** (N - 1)
dist = 2 ** (N - 1)
for i in reversed(list(range(X.bit_length()))):
    if X & (1 << i):
        ans.append((0, N - i - 1, dist))
        dist += (2 ** i)


print((N, len(ans)))
for a, b, d in ans:
    print((a + 1, b + 1, d))
