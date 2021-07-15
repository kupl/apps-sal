n, k = list(map(int,input().split()))

a = list(map(int,input().split()))

cnt1 = 0
for i in range(n):
    cnt1 += a[i] % 2
ans = ['Daenerys' , 'Stannis']
if(n == k):
    print(ans[sum(a)%2])
    return
if(cnt1 > (n - k)//2 and (n - cnt1) > (n - k)//2):
    print(ans[(n - k) % 2])
else:
    if(cnt1 > (n - k) //2):
        cnt0 = n - cnt1
        print(ans[(sum(a) - ((n - k) - cnt0))%2])
        
    else:
        
        print(ans[(sum(a) - cnt1)%2])

        

    

