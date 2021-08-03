N = int(input())

d = dict()
for i in range(1, N + 1):
    _0 = str(i)[0]
    _1 = str(i)[-1]
    if _1 == "0":
        continue
    s = _0 + _1
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

res = 0
for i in range(1, N + 1):
    _0 = str(i)[0]
    _1 = str(i)[-1]
    if _1 == "0":
        continue
    s = _1 + _0
    if s in d:
        res += d[s]

print(res)
