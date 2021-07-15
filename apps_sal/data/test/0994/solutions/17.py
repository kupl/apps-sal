[n, k] = [int(x) for x in input().split()]
Data = type('Data', (object,), {'index': 0, 'value': 0})

data = [Data() for _ in range(k)]
for i in range(k):
    [data[i].index, data[i].value] = [int(x) for x in input().split()]

data.sort(key=lambda x: x.index)

ans = max(data[0].value + data[0].index - 1, data[k-1].value + n - data[k-1].index)

for i in range(1, k):
    L = data[i].index - data[i-1].index
    minH = min(data[i].value, data[i-1].value)
    maxV = max(data[i].value, data[i-1].value)

    if minH + L < maxV:
        ans = -1
        break

    ans = max(ans, (L + minH + maxV) // 2)

if ans < 0:
    print("IMPOSSIBLE")
else:
    print(ans)

