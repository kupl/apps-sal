def go():
    n, h, l, r = list(map(int, input().split()))
    # n = int(input())
    a = list(map(int, input().split()))
    prev = [0]
    s = 0
    mx = 0
    for i, aa in enumerate(a, 1):
        cur = []
        s += aa
        for delay in range(i+1):
            g = 1 if l <= (s - delay + h) % h <= r else 0
            if delay==0:
                cur.append(prev[delay]+g)
            elif delay==i:
                cur.append(prev[delay-1] + g)
            else:
                cur.append(max(prev[delay],prev[delay-1])+g)
        prev = cur
        mx = max(mx,max(cur))
    return mx


# t = int(input())
for _ in range(1):
    print(go())

