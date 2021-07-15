def search(n):
    s = 1
    e = n
    while(s<=e):
        mid = (s+e)//2
        if((mid*(mid+1)//2) <= n):
            ans = mid
            s = mid+1
        else:
            e = mid-1
    return ans
n = int(input())
print((1 + n - search(n+1)))

