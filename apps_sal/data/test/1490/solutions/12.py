n, m = list(map(int, input().split()))
has = list(map(int, input().split()))
has.sort()
res = []
uc = 0
for i in range(1, 10 ** 9 + 1):
    if uc < len(has) and has[uc] == i:
        uc += 1
    elif m - i < 0:
        break
    else:
        m -= i
        res.append(i)
print(len(res))
print(*res)
