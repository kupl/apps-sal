k, n, *l = map(int, open(0).read().split())
l += [l[0] + k]
print(k - max(l[i + 1] - l[i] for i in range(n)))
