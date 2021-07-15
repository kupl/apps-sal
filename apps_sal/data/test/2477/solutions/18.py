def is_ok(x):
    sum=0
    for i in range(n):
        sum+=(a[i]+x-1)//x-1
    if sum<=k:return True
    else :return False

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n,k=map(int,input().split())
a=list(map(int,input().split()))
if is_ok(1):
    print(1)
    return
print(meguru_bisect(1,int(1e10)))
