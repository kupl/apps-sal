import sys

N = int(input()); A = list(map(int,input().split()))

if N == 2:
    print(max(A))
    return

dp = [0,max(A[:3]),A[0]+A[2]]
tmp1 = dp[:]
tmp2 = [0,max(A[:2]),0]
flag1 = False
flag2 = True if A[0] < A[2] and A[1] < A[2] else False
flag3 = False

for i in range(3,N):
    b = A[i]
    if i%2 == 0:
        dp[0] = max(tmp2[0],tmp1[0]+b)
        flag1 = True if tmp2[0] < tmp1[0]+b else False
        if flag3:
            dp[1] = max(tmp2[1],tmp1[1]+b)
            flag2 = True if tmp2[1] < tmp1[1]+b else False 
        else:
            dp[1] = max(tmp2[1],tmp2[0]+b,tmp1[1]+b)
            flag2 = True if tmp2[1] < tmp2[0]+b or tmp2[1] < tmp1[1]+b else False 
        dp[2] += A[i]
        tmp1 = dp[:]
    else:
        if flag1:
            dp[0] = max(tmp1[1],tmp2[0]+b)
            flag3 = True if tmp1[1] < tmp2[0]+b else False
        else:
            dp[0] = max(tmp1[1],tmp1[0]+b,tmp2[0]+b)
            flag3 = True if tmp1[1] < tmp1[0]+b or tmp1[1] < tmp2[0]+b else False
        if flag2:
            dp[1] = max(tmp1[2],tmp2[1]+b)
        else:
            dp[1] = max(tmp1[2],tmp1[1]+b,tmp2[1]+b)
        tmp2 = dp[:]
        
print (dp[1])
