n = int(input())
arr = list(map(int, input().split()))
idx, res = 0, []
m = int(input())
for _ in range(m):
    w, h = map(int, input().split())
    r = max(arr[w - 1], idx)
    res.append(r)
    arr[w - 1] = r + h
    idx = max(idx, arr[w - 1])
print('\n'.join(map(str, res)))
