n, k = map(int, input().split())
t = [i for i, v in enumerate(input()) if v == '0']
s, i = n, 0
a, b = t[:2]
for l, r in zip(t, t[k:]):
    while max(r - a, a - l) > max(r - b, b - l): 
        i += 1
        a, b = t[i:i + 2]
    s = min(s, max(r - a, a - l))
print(s)
