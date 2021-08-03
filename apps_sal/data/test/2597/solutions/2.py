q = int(input())
for fwe in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l.reverse()
    wyn = 0
    while True:
        if wyn == n:
            break
        if wyn < l[wyn]:
            wyn += 1
        else:
            break
    print(wyn)
