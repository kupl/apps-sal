(m, k) = map(int, input().split())
ret = []
if k >= 2 ** m or (m == 1 and k == 1):
    ret.append(-1)
elif m == 1:
    ret = [0, 0, 1, 1]
else:
    ret.append(k)
    for i in range(2 ** m):
        if i != k:
            ret.append(i)
    ret.append(k)
    for i in range(2 ** m - 1, -1, -1):
        if i != k:
            ret.append(i)
print(' '.join(map(str, ret)))
