def solve(n,h,v,A):
    cnt = 0
    curh = A[0]
    for i in range(1,n):
        if A[i]+curh<=h:
            curh += A[i]
        else:
            quan = int((A[i]+curh-h)/v) + ((A[i]+curh-h) % v > 0)
            cnt += quan
            curh = max(curh - quan*v, 0)
            curh += A[i]
    cnt += int(curh/v) + (curh % v > 0)
    return cnt
    
(n,h,k) = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(solve(n,h,k,A))
