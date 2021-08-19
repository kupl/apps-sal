vals = list(map(int, input().split()))
(min_val, max_val) = sorted(vals)
ret = ''
for i in range(max_val):
    ret += str(min_val)
print(ret)
