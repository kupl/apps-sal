n, k = map(int, input().split())
res = 0
for i in range(k+1,n+1):
    res += (n // i) * (i - k)
    if  n%i != 0:
        res += max(n%i-max(k-1,0),0)
print(res)
