(H, W, N) = map(int, input().split())
direc = [[0, 0], [-1, 0], [-2, 0], [0, -1], [-1, -1], [-2, -1], [0, -2], [-1, -2], [-2, -2]]
dic = {}
for i in range(N):
    (h, w) = map(int, input().split())
    for d in direc:
        if 1 <= h + d[0] <= H - 2 and 1 <= w + d[1] <= W - 2:
            l = (h + d[0], w + d[1])
            if l in dic:
                dic[l] = dic[l] + 1
            else:
                dic[l] = 1
A = list(dic.values())
print((H - 2) * (W - 2) - len(A))
for i in range(1, 10):
    print(A.count(i))
