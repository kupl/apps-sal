(a, b, c, d) = map(int, input().split())
res = -float('inf')
for x in [a, b]:
    for y in [c, d]:
        res = max(x * y, res)
print(res)
