def gcd(x, y):
    if(y > x):
        tmp = y
        y = x
        x = tmp

    while(int(x%y)>0):
        r = x%y
        x = y
        y = r

    return y
        


n = int(input())
a = list(map(int, input().split()))

ans = gcd(a[0], a[1])
for i in range(1, n-1):
    ans = min(ans, gcd(a[i], a[i+1]))

print(ans)
