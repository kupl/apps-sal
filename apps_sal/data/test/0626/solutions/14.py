n = int(input())
L = list(map(int, input().split()))
P = [ 0 for _ in range(n)]
r = 0
t = 0
while t < n:
    for k in range(n):
        if P[k] == 0 and L[k] <= t:
            t+=1
            P[k] = 1
    r+=1
    if t == n:
        break
    for k in range(n):
        if P[n-k-1] == 0 and L[n-k-1] <= t:
            t+=1
            P[n-k-1] = 1
    r+=1
print(r-1)
