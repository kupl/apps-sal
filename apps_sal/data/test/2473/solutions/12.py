N, K = list(map(int, input().split()))
xy = []
for _ in range(N):
    xy.append(tuple(map(int, input().split())))

xy = sorted(xy, key=lambda x: x[0])
# print(xy)

lst = []
for left in range(0, N - K + 1):
    for right in range(left + K - 1, N):
        #print(left, right)
        W = xy[right][0] - xy[left][0]
        # print(W)
        temp = sorted(xy[left:right + 1], key=lambda x: x[1])
        # print(temp)
        # 含まれる点の個数はright-left+1個
        for bottom in range(0, right - left + 1 - K + 1):
            #print('W', W, 'bottom',bottom)
            H = temp[bottom + K - 1][1] - temp[bottom][1]
            #print('H', H)
            lst.append(H * W)
# print('lst',lst)
print((min(lst)))
