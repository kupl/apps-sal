n = int(input())
k = int(input())
A = int(input())
B = int(input())

res = 0
while n>k:
    if n % k >0:
        res += (n%k) * A
        n -= (n%k)

    dif  = n - (n//k)
    if dif*A > B:
        res += B
        n = n//k
    else:
        res += (n-1)*A
        n = 1

if n == k:
    dif  = n - (n//k)
    if dif*A > B:
        res += B
        n = n//k
    else:
        res += (n-1)*A
        n = 1

if n >1 :
    res += (n-1)*A
    n = 1
print(res)

