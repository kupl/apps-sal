t = int(input())
for t in range(t):
    n, k = [int(i) for i in input().split(" ")]
    a = [int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]
    for i in range(k):
        aMin = min(a)
        bMax = max(b)
        if bMax > aMin:
            a[a.index(aMin)], b[b.index(bMax)] = b[b.index(bMax)], a[a.index(aMin)]
    print(sum(a))
