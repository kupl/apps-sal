N, K = map(int, input().split())
xy = []
for i in range(N):
    xy.append(tuple(map(int, input().split())))
xy = sorted(xy, key=lambda x: x[0])
lst = []
for left in range(0, N - K + 1):
    for right in range(left + K - 1, N):
        W = xy[right][0] - xy[left][0]
        temp = sorted(xy[left:right + 1], key=lambda x: x[1])
        for bottom in range(0, right - left + 1 - K + 1):
            H = temp[bottom + K - 1][1] - temp[bottom][1]
            lst.append(H * W)
print(min(lst))
