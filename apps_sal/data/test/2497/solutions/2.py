n = int(input())
R = []
L = []
U = []
D = []
lm = [float("INF")] * 3
rm = [-float("INF")] * 3
dm = [float("INF")] * 3
um = [-float("INF")] * 3
for i in range(n):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    if d == "U":
        rm[1] = max(rm[1], x)
        lm[1] = min(lm[1], x)
        dm[0] = min(dm[0], y)
        um[2] = max(um[2], y)
        U.append((x, y, d))
    elif d == "D":
        rm[1] = max(rm[1], x)
        lm[1] = min(lm[1], x)
        um[0] = max(um[0], y)
        dm[2] = min(dm[2], y)
        D.append((x, y, d))
    elif d == "L":
        um[1] = max(um[1], y)
        dm[1] = min(dm[1], y)
        rm[0] = max(rm[0], x)
        lm[2] = min(lm[2], x)
        L.append((x, y, d))
    else:
        um[1] = max(um[1], y)
        dm[1] = min(dm[1], y)
        lm[0] = min(lm[0], x)
        rm[2] = max(rm[2], x)
        R.append((x, y, d))
time = set()


def rc(t):
    if rm[2] == max(rm):
        return rm[2] + t
    if rm[1] == max(rm):
        if rm[2] == -float("INF"):
            return rm[1]
        else:
            time.add(rm[1] - rm[2])
            return max(rm[1], rm[2] + t)
    if rm[2] == -float("INF") and rm[1] == -float("INF"):
        return rm[0] - t
    if rm[2] == -float("INF"):
        time.add(rm[0] - rm[1])
        return max(rm[1], rm[0] - t)
    if rm[1] == -float("INF"):
        time.add((rm[0] - rm[2]) / 2)
        return max(rm[0] - t, rm[2] + t)
    if (rm[0] - rm[2]) / 2 + rm[2] >= rm[1]:
        time.add((rm[0] - rm[2]) / 2)
        return max(rm[0] - t, rm[2] + t)
    time.add(rm[0] - rm[1])
    time.add(rm[1] - rm[2])
    return max(rm[0] - t, rm[2] + t, rm[1])


def lc(t):
    if lm[2] == min(lm):
        return lm[2] - t
    if lm[1] == min(lm):
        if lm[2] == float("INF"):
            return lm[1]
        else:
            time.add(-lm[1] + lm[2])
            return min(lm[1], lm[2] - t)
    if lm[2] == float("INF") and lm[1] == float("INF"):
        return lm[0] + t
    if lm[2] == float("INF"):
        time.add(-lm[0] + lm[1])
        return min(lm[1], lm[0] + t)
    if lm[1] == float("INF"):
        time.add((-lm[0] + lm[2]) / 2)
        return min(lm[0] + t, lm[2] - t)
    if lm[2] - (-lm[0] + lm[2]) / 2 <= lm[1]:
        time.add((-lm[0] + lm[2]) / 2)
        return min(lm[0] + t, lm[2] - t)
    time.add(-lm[0] + lm[1])
    time.add(-lm[1] + lm[2])
    return min(lm[0] + t, lm[2] - t, lm[1])


def uc(t):
    if um[2] == max(um):
        return um[2] + t
    if um[1] == max(um):
        if um[2] == -float("INF"):
            return um[1]
        else:
            time.add(um[1] - um[2])
            return max(um[1], um[2] + t)
    if um[2] == -float("INF") and um[1] == -float("INF"):
        return um[0] - t
    if um[2] == -float("INF"):
        time.add(um[0] - um[1])
        return max(um[1], um[0] - t)
    if um[1] == -float("INF"):
        time.add((um[0] - um[2]) / 2)
        return max(um[0] - t, um[2] + t)
    if (um[0] - um[2]) / 2 + um[2] >= um[1]:
        time.add((um[0] - um[2]) / 2)
        return max(um[0] - t, um[2] + t)
    time.add(um[0] - um[1])
    time.add(um[1] - um[2])
    return max(um[0] - t, um[2] + t, um[1])


def dc(t):
    if dm[2] == min(dm):
        return dm[2] - t
    if dm[1] == min(dm):
        if dm[2] == float("INF"):
            return dm[1]
        else:
            time.add(-dm[1] + dm[2])
            return min(dm[1], dm[2] - t)
    if dm[2] == float("INF") and dm[1] == float("INF"):
        return dm[0] + t
    if dm[2] == float("INF"):
        time.add(-dm[0] + dm[1])
        return min(dm[1], dm[0] + t)
    if dm[1] == float("INF"):
        time.add((-dm[0] + dm[2]) / 2)
        return min(dm[0] + t, dm[2] - t)
    if dm[2] - (-dm[0] + dm[2]) / 2 <= dm[1]:
        time.add((-dm[0] + dm[2]) / 2)
        return min(dm[0] + t, dm[2] - t)
    time.add(-dm[0] + dm[1])
    time.add(-dm[1] + dm[2])
    return min(dm[0] + t, dm[2] - t, dm[1])


ans = (rc(0) - lc(0)) * (uc(0) - dc(0))
for t in time:
    count = (rc(t) - lc(t)) * (uc(t) - dc(t))
    ans = min(ans, count)
print(ans)
