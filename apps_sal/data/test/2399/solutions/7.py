def sol():
    a, b = map(int, input().split())
    s = input().replace("X", " ")
    small_segs = 0
    critical_region = -1

    for p in map(len, s.split()):
        if p < b:
            continue
        if p < a and p >= b:
            return False
        if ((p - a) % 2 == 0 and (p >= a + 4 * b)) or ((p - a) % 2 == 1 and p >= a + 4 * b - 1):
            return False
        if p >= 2*b:
            if critical_region != -1:
                return False
            critical_region = p
        elif p >= a:
            small_segs += 1
    
    if critical_region == -1:
        return small_segs % 2 == 1

    can = [0] * 3
    for l in range(critical_region+1-a):
        r = critical_region - l - a
        if (l >= b and l < a) or l >= 2 * b:
            continue
        if (r >= b and r < a) or r >= 2 * b:
            continue
        canl = int(l >= a)
        canr = int(r >= a)
        can[canl + canr] = 1

    for choice, val in enumerate(can):
        if val and (small_segs + choice) % 2 == 0:
            return True

    return False



n = int(input())

for _ in range(n):
    print("YES" if sol() else "NO")
