k, n = map(int, input().split())
a = list(map(int, input().split()))

d = [0]*n
for i in range(n):
    if i == n-1:
        d[n-1] = (k-a[n-1]) + a[0]
        
    else :
        d[i] = a[i+1] - a[i]

d.sort()
d[n-1] = 0

print(sum(d))
