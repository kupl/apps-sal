def R():
    return map(int, input().split())


(n, k) = R()
arr = list(R())
tup = [0, 0]
res = 0
for x in arr:
    if x != 0:
        (tup[0], tup[1]) = (tup[0] + x, tup[1] + x)
        tup[1] = min(tup[1], k)
    elif tup[1] < 0:
        (tup[0], tup[1]) = (0, k)
        res += 1
    else:
        tup[0] = max(0, tup[0])
    if tup[0] > k:
        res = -1
        break
print(res)
