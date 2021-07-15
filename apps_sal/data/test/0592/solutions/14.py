n = int(input())

ans = 0
for i in range(2,n//2+1):
    x = n // i 
    ans +=  ( x * (x+1) // 2 - 1 ) * 4
print(ans)    

