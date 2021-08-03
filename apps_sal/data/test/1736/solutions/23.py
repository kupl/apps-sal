n, t = list(map(int, input().split()))
A = list(map(int, input().split()))
d = 0
f = 1
s = A[0]
r = 0 + (s <= t)
while f < n:
    while s <= t and f < n:
        s += A[f]
        f += 1
    r = max(r, f - d - (s > t))
    if f == n:
        break
    while s > t:
        s -= A[d]
        d += 1
print(r)
