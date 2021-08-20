from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    counts = defaultdict(int)
    for x in w:
        counts[x] += 1
    m = 0
    for s in range(2, n * 2 + 1):
        count = 0
        for x in list(counts.keys()):
            xcount = counts[x]
            if x < s - x:
                c = counts[s - x]
                count += min(c, xcount)
            elif x == s - x:
                count += xcount // 2
        m = max(m, count)
    print(m)
