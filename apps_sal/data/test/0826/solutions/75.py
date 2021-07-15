n = int(input())
right =  10**18+1
left =  -1
while right - left >1:
    mid =  (right+left) // 2
    if mid*(mid+1)//2 > n+1:
        right = mid
    else:
        left = mid
        
print(n-left+1)
