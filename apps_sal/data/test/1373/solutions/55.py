n, k = map(int,input().split())
cnt = 0
for i in range(k,n+2):
    cnt += i*n -(i-1)*i +1  
print(cnt%(10**9+7)) 
