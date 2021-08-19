(n, a, b) = map(int, input().split())
l = [int(x) for x in input().split()]
res = 0
for i in range(n // 2):
    (x, y) = (l[i], l[-1 - i])
    if 2 in [x, y]:
        if x == y:
            res += 2 * min(a, b)
        else:
            res += a if min(x, y) == 0 else b
    elif x != y:
        res = -1
        break
if n % 2 == 1 and res != -1 and (l[n // 2] == 2):
    res += min(a, b)
print(res)
