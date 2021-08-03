def f(): return map(int, input().split())


n, k = f()
a, b, c, d = f()
s = list(set(range(1, n + 1)).difference({a, b, c, d}))
d = [a, c] + s + [d, b] + [c, a] + s + [b, d]
print(' '.join(map(str, d)) if 4 < n < k else -1)
