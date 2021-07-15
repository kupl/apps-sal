for tc in range(int(input())):
    n,m = list(map(int, input().split()))
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    aidx = {}
    for i,e in enumerate(al):
        aidx[e]=i
    midx = -1
    res = 0
    for i,e in enumerate(bl):
        idx = aidx[e]
        if idx <= midx:
            res += 1
        else:
            res += 2*(idx-i)+1
        midx = max(midx, idx)
    print(res)

