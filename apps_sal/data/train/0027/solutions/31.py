t = int(input())
for i in range(t):
    n = int(input())
    a = list([bin(int(x))[2:] for x in input().split()])
    d = dict()
    for i in a:
        ir = i.rfind("1")
        c = len(i) - ir - 1
        raw = int(i[:ir + 1], base=2)
        d[raw] = max(d.get(raw, c), c)
    print(sum(d.values()))
