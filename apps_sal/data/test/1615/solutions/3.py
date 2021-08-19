(n, k) = map(int, input().split())
print((sum((int(l) - int(r) for (l, r) in [input().split() for i in range(n)])) - n) % k)
