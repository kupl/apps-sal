(l, r, a) = list(map(int, input().split()))
if l > r:
    (l, r) = (r, l)
b = min(r - l, a)
total = (l + b) * 2 + (a - b) // 2 * 2
print(total)
