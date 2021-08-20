T = int(input())
for _ in range(T):
    n = int(input())
    seg = []
    for s in range(n):
        (l, r) = [int(x) for x in input().split()]
        seg.append((l, r))
    pos = {}
    for i in range(n):
        if seg[i] in pos:
            pos[seg[i]].append(i)
        else:
            pos[seg[i]] = [i]
    seg.sort()
    right = seg[0][1]
    goodindex = -1
    for j in range(1, n):
        if seg[j][0] > right:
            goodindex = j
            break
        right = max(right, seg[j][1])
    if goodindex == -1:
        print(-1)
    else:
        ans = ['2'] * n
        for i in range(goodindex):
            ans[pos[seg[i]][-1]] = '1'
            pos[seg[i]].pop()
        print(' '.join(ans))
