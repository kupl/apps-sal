N, x = map(int,input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(N-1):
    if a[i] + a[i+1] > x:
        temp = a[i] + a[i+1] - x 
        if a[i+1] - temp >= 0:
            ans += temp
            a[i+1] -= temp
        else:
            ans += temp
            a[i+1] = 0
            a[i] -= temp - a[i+1]
     
print(ans)
