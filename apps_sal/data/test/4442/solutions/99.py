vals = list(map(int, input().split()))

min_val, max_val = sorted(vals)

ret = str(min_val) * max_val

print(ret)
