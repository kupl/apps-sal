f = lambda: list(map(int, input().split()))
n, k = f()
d = sum(q & 1 for q in f())
s = n - k >> 1
q = s < d and (k & 1 or s < n - d) if n - k & 1 else k & 1 and s >= n - d
if n == k: q = d & 1
print(['Daenerys', 'Stannis'][q])

