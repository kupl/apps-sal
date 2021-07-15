M,K = map(int,input().split())

num = 2**(M+1)

if K >= num//2 or (M==1 and K==1):
    ans = [-1]
elif M==1 and K==0:
    ans = [0,0,1,1]
else:
    ans = [0]*num
    for i in range(2**M):
        if i==K: continue
        ans[i-(i>K)] = i
        ans[num-2-i+(i>K)] = i
    ans[num//2-1] = K
    ans[-1] = K
    
print(*ans)
