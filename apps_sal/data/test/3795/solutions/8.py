n = int(input())
d = int(input())
e = int(input()) * 5
(d, e) = (max(d, e), min(d, e))
v = n
for i in range(e):
    m = n - i * d
    if m < 0:
        break
    m %= e
    v = min(v, m)
print(v)
