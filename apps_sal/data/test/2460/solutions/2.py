n, m = list(map(int, input().split()))
xs = [int(k) for k in input().split()]
ts = [int(k) for k in input().split()]
pos = [-1 for i in range(n + m)]
if ts[0]:
    pos[0] = 0
for i in range(1, n + m):
    pos[i] = pos[i - 1]
    if ts[i]:
        pos[i] += 1
result = [0 for i in range(m)]
left = 0
leftC = 0
right = 0
rightC = 0
for i in range(n + m):
    if ts[i] == 0:
        right = max(i, right)
        while right + 1 < n + m and not ts[right]:
            right += 1
        mP, mD = 0, 20000000
        if ts[left]:
            mP = pos[left]
            mD = xs[i] - xs[left]
        if ts[right] and xs[right] - xs[i] < mD:
            mD = xs[right] - xs[i]
            mP = pos[right]
        result[mP] += 1
    else:
        left = i
print(*result)
