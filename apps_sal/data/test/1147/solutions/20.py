from bisect import bisect_left as b
f = lambda: map(int, input().split())
n, x, k = f()
s, t = 0, sorted(f())
p = [(q, ((q - 1) // x + k) * x) for q in t]
for q, d in p: s += b(t, d + x) - b(t, max(q, d))
print(s)
