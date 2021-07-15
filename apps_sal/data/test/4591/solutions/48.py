a, b, c, x, y = list(map(int, input().split()))

ans = 10**10
for i in range(10**5+1):
    price = a*max(x-i, 0) + b*max(y-i, 0)+ i*2*c 
    ans = min(ans, price)
print(ans)

