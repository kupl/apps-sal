a, b, x = map(int, input().split())

max_val, min_val = 10**9 + 1, 0
while max_val - min_val > 1:
    mid_val = (max_val + min_val) // 2
    c = a * mid_val + b * len(str(mid_val))
    if c <= x:
        min_val = mid_val
    else:
        max_val = mid_val
print(min_val)
