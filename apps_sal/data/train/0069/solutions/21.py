for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    arr = list(map(int,list(input())))+[0]
    n = len(arr)
    now = 0
    lastEnds = 0
    fl = False
    lenghts = []
    dists = []
    for i in range(n):
        if fl and not arr[i]:
            if len(lenghts):
                dists.append(i-lastEnds-now)
            lenghts.append(now)
            fl = False
            now = 0
            lastEnds = i
        elif fl and arr[i]:
            now+=1
        elif not fl and arr[i]:
            fl = True
            now = 1

    price = a
    if len(lenghts) == 0:
        price = 0

    for i in range(len(dists)):
        if dists[i]*b<a:
            price+=dists[i]*b
        else:
            price+=a

    print(price)

