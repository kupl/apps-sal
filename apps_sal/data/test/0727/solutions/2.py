import heapq

n = int(input())
a = list(map(int, input().split()))

# idx: l, r, length, val
d = {}
pre, l = None, 0
seg = []

for i, x in enumerate(a):
    if pre is None:
        pre = x
        l = 1
    else:
        if x == pre:
            l += 1
        else:
            seg.append([l, pre])
            pre = x
            l = 1

    if i == len(a) - 1:
        seg.append([l, x])

Q = []
for i, s in enumerate(seg):
    l = None if i == 0 else i - 1
    r = None if i + 1 == len(seg) else i + 1
    d[i] = [l, r, s[0], s[1]]

    heapq.heappush(Q, (-s[0], i))

cnt = 0
while len(Q) > 0:
    length, idx = heapq.heappop(Q)
    length = -length

    # print(d[idx])
    if d[idx][2] != length:
        continue

    l, r, length, val = d[idx]
    d[idx][0] = 0
    cnt += 1

    if l is None and r is None:
        break
    elif l is None:
        d[r][0] = None
    elif r is None:
        d[l][1] = None
    else:
        if d[l][3] == d[r][3]:
            d[l][1] = d[r][1]
            d[l][2] += d[r][2]
            d[r][2] = 0

            if d[r][1] is not None:
                nnr = d[r][1]
                d[nnr][0] = l

            heapq.heappush(Q, (-d[l][2], l))
        else:
            d[l][1] = r
            d[r][0] = l
print(cnt)
