def __starting_point():
    arr = input().split(' ')
    c = []
    for a in arr:
        c.append(int(a))
    ans = min(c[3],2*c[2])
    arr = input().split(' ')
    n = int(arr[0])
    m = int(arr[1])
    an = []
    am = []
    arr = input().split(' ')
    for a in arr:
        an.append(int(a))
    arr = input().split(' ')
    for a in arr:
        am.append(int(a))
    ca = 0
    for a in an:
        if a*c[0]<c[1]:
            ca+=a*c[0]
        else:
            ca+=c[1]
    ca=min(ca,c[2])
    cb = 0
    for a in am:
        if a*c[0]<c[1]:
            cb+=a*c[0]
        else:
            cb+=c[1]
    cb = min(cb,c[2])
    ans = min(ans,ca+cb)
    print(ans)
            

__starting_point()
