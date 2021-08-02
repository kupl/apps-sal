import sys
# sys.stdin = open('input.txt')
n, q = list(map(int, input().split()))
scanline = [0] * n
mal = []
ans = 0
for i in range(q):
    a, b = list(map(int, input().split()))
    a -= 1
    mal.append((a, b))
    scanline[a] += 1
    if b < n:
        scanline[b] -= 1

for i in range(q):
    scanline[mal[i][0]] -= 1
    if mal[i][1] < n:
        scanline[mal[i][1]] += 1
    ots = [0] * (n + 1)
    not0 = 0
    cur = 0
    inans = -10000000000
    # print(scanline)
    for j in range(1, n + 1):
        cur += scanline[j - 1]
        if cur != 0:
            not0 += 1
        if cur == 1:
            ots[j] = ots[j - 1] + 1
        else:
            ots[j] = ots[j - 1]
    # print(ots)
    for j in range(q):
        if j == i:
            continue
        inans = max(inans, ots[mal[j][0]] - ots[mal[j][1]])
    # print(inans)
    ans = max(ans, inans + not0)
    scanline[mal[i][0]] += 1
    if mal[i][1] < n:
        scanline[mal[i][1]] -= 1
print(ans)
