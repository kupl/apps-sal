n = int(input())
res = None
for i in range(n):
    its = [int(k) for k in input().split()]
    s = set(its[1:])
    if res is None:
        res = s
    else:
        res &= s
print(*res)

