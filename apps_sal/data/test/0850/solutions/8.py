k = int(input())
ds = list(map(int, input().split()))
es = []
bs = [False, False, False]
for d in ds:
    assert 0 <= d <= 100
    if d == 0:
        es.append(d)
    elif 1 <= d <= 9:
        if not bs[0]:
            bs[0] = True
            es.append(d)
    elif 10 <= d <= 99 and d % 10 == 0:
        if not bs[1]:
            bs[1] = True
            es.append(d)
    elif d == 100:
        if not bs[2]:
            bs[2] = True
            es.append(d)
for d in ds:
    if not bs[0] and (not bs[1]):
        if 10 <= d <= 99 and d % 10 != 0:
            bs[0] = True
            bs[1] = True
            es.append(d)
print(len(es))
print(*es)
