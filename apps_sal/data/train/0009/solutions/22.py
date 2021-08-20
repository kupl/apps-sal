t = int(input())
for _ in range(t):
    s = [int(i) for i in input().strip()]
    n = len(s)
    bckt = []
    ct = 0
    for i in range(n):
        if s[i]:
            ct += 1
        elif ct:
            bckt.append(ct)
            ct = 0
    if ct:
        bckt.append(ct)
    bckt.sort(reverse=True)
    print(sum(bckt[::2]))
