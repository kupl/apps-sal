(n, m) = map(int, input().split())
arr = {}
for _ in range(m):
    (a, b) = map(str, input().split())
    if len(a) > len(b):
        arr[a] = b
lect = input().split()
res = []
for i in lect:
    if i in arr:
        res.append(arr[i])
    else:
        res.append(i)
print(' '.join(res))
