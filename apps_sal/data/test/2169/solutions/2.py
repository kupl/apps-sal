h, w, d = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

nums = {}
for i in range(h):
    for j in range(w):
        nums[a[i][j]] = (i, j)

acc = [0] * (h * w)
for i in range(h * w):
    if i >= d:
        _to = nums[i + 1]
        _from = nums[i + 1 - d]
        acc[i] += acc[i - d] + abs(_from[0] - _to[0]) + abs(_from[1] - _to[1])

for l, r in lr:
    print((acc[r - 1] - acc[l - 1]))
