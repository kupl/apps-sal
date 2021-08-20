(n, k) = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(arr[i], i) for i in range(n)]
arr.sort()
t = 0
res = []
for i in arr:
    res.append(i)
    if sum([i[0] for i in res]) > k:
        res = res[:-1]
        break
if len(res) == 0:
    print('0')
else:
    print(len(res))
    print(' '.join([str(i[1] + 1) for i in res]))
