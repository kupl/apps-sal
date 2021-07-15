def isok(arg):
    count = arg
    for i in range(n):
        if -(-(h[i]-b*arg)//(a-b)) >= 0:
            count -= -(-(h[i]-b*arg)//(a-b))
    if count >= 0:
        return True
    else:
        return False

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n,a,b = list(map(int,input().split()))
h = []
for i in range(n):
    h.append(int(input()))
print((bisect(0,10**9)))

