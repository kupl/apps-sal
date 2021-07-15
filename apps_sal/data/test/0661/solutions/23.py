def solve():
    M, K = map(int, input().split())
    if K>=1<<M:
        return [-1]
    if M==1:
        if K==0:
            return [1,0,0,1]
        return [-1]
    ans = [K]
    for i in range(1<<M):
        if i!=K:
            ans.append(i)
    ans.append(K)
    for i in range((1<<M)-1,-1,-1):
        if i!=K:
            ans.append(i)
    return ans
print(*solve())
