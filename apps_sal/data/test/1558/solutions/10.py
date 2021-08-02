from sys import stdin


def main():
    n, r, avg = list(map(int, stdin.readline().strip().split()))
    aa, bb = [], []
    for _ in range(n):
        a, b = list(map(int, stdin.readline().strip().split()))
        aa.append(a)
        bb.append(b)
    now = sum(aa)
    ineed = n * avg
    if now >= ineed:
        return 0
    pref = sorted(list(range(n)), key=bb.__getitem__)
    tot = 0
    for i in pref:
        a, b = aa[i], bb[i]
        delta = min(ineed - now, r - a)
        tot += b * delta
        now += delta
        if now == ineed:
            return tot


print(main())
