(n, m) = [int(c) for c in input().split()]
a = [int(c) for c in input().split()]
res = 0
current_sum = 0
while len(a) > 0:
    val = a.pop()
    if current_sum + val <= m:
        current_sum = current_sum + val
    else:
        current_sum = val
        res += 1
if current_sum != 0:
    res += 1
print(res)
