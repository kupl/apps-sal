def c(n):
    
    ans = 0
    if n > 15:
        ans += (49 * (n - 15))
        n = 15
    l = set()
    for i in range(max(n+1,441)):
        for j in range(max(n-i+1,196)):
            for k in range(n-i-j+1):
                l.add(i*4+j*9+k*49)
    return ans + len(l)
n = int(input())
print(c(n))

