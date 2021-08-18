a, b, c, k = map(int, input().split())

max_val = 0
if k <= a:
    max_val += k
else:
    max_val += a
    k -= a
    if k <= b:
        pass
    else:
        k -= b
        max_val -= k

print(max_val)
