def bs(arr,m):
    n=len(arr)    
    low = 0
    high = n 
    while (low != high):
        mid = (low + high) // 2
        if (arr[mid] <= m):
            low = mid + 1
        else:
            high = mid
    return low

n=int(input())
ip=list(map(int,input().split()))
ip=sorted(ip)
for i in range(int(input())):
    m=int(input())
    print(bs(ip,m))

