f = lambda: map(int, input().split())
n, x, k = f()
t = sorted(f())
s = i = j = 0
for y in t:
    d = (y // x - k) * x
    while i < n and t[i] <= min(d, y): i += 1
    while j < n and t[j] <= min(d + x, y): j += 1
    s += j - i
print(s)
