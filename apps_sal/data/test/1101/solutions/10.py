n, k = list(map(int, input().split()))
t = [i for i, v in enumerate(input()) if v == '0']
s, m = n, 0
f = lambda m: max(r - t[m], t[m] - l)
for l, r in zip(t, t[k:]):
    while f(m) > f(m + 1): m += 1
    s = min(s, f(m))
print(s)

