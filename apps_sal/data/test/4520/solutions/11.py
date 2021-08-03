n, k = map(int, input().split())
N = 2 * 10 ** 5 + 1
pre = [0] * (N + 1)
seg = []
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    seg.append([y, -x, i + 1])
    pre[x] += 1
    pre[y + 1] -= 1
seg.sort()
seg.reverse()
seg = [[-seg[i][1], seg[i][0], seg[i][2]] for i in range(len(seg))]
cov = [0] * (N + 1)
cov[0] = pre[0]
for i in range(1, N):
    cov[i] = cov[i - 1] + pre[i]
wyn = 0
ziomy = []
for i in range(N):
    p = 0
    while cov[i] > k:
        maksi = -1
        opti = -1
        mini = 100000000000
        for d in range(len(seg)):
            if seg[d][1] > maksi and seg[d][0] <= i:
                mini = 100000000000000
                maksi = seg[d][1]
                opti = d
            elif seg[d][1] == maksi and seg[d][0] < mini and seg[d][0] <= i:
                mini = seg[d][0]
                opti = d
        pt = seg[opti][1]
        ziomy.append(seg[opti][2])
        pre[pt + 1] += 1
        pre[i] -= 1
        cov[i] -= 1
        p += 1
        seg.pop(opti)
    cov[i + 1] = cov[i] + pre[i + 1]
    wyn += p
print(wyn)
print(*ziomy)
