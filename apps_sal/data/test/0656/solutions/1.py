def solve(k, s):
    w = [0]
    for c in s:
        if c < 0:
            if w[-1] >= 0:
                w.append(-1)
            else:
                w[-1] -= 1
        elif w[-1] < 0:
            w.append(1)
        else:
            w[-1] += 1
    (begin, end) = (w[0], w[-1])
    if len(w) == 1 and w[0] > 0:
        return 0
    if begin > 0:
        w.pop(0)
    if end > 0:
        w.pop()
    neg_seg = [t for t in w if t < 0]
    pos_seg = [t for t in w if t > 0]
    d = -sum(neg_seg)
    if d > k:
        return -1
    changes = 2 * len(neg_seg) - (end < 0)
    pos_seg.sort()
    for seg in pos_seg:
        d += seg
        if d > k:
            if end > 0 and d - seg + end <= k:
                return changes - 1
            else:
                return changes
        else:
            changes -= 2
    if end > 0 and d + end <= k:
        return changes - 1
    else:
        return changes


(n, k) = list(map(int, input().split()))
s = [int(x) for x in input().split()]
print(solve(k, s))
