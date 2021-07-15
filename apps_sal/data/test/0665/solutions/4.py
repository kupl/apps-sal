for tc in range(int(input())):
    n,tottime = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    if sum(ls) <= tottime:
        print(0)
        continue
    mxseen = 0
    mxidx = 0
    totsofar = 0
    for i,e in enumerate(ls):
        if totsofar + e - max(e,mxseen) > tottime:
            break
        totsofar += e
        if mxseen < e:
            mxseen = e
            mxidx = i+1
        if totsofar-mxseen > tottime:
            break
    print(mxidx)

