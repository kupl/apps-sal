n,a,b = (int(i) for i in input().split())
ans = [[0 for i in range(b)] for j in range(a)]
if n>a*b:
    print(-1)
else:
    k = 1
    for i in range(a):
        for j in range(b):
            if n == 0 :
                break
            else:
                ans[i][j] = k
                k+=1
                n-=1
    if b%2 == 1:
        for i in range(a):
            print(' '.join(list(map(str,ans[i]))))
    else:
        for i in range(a):
            if i%2 == 0:
                print(' '.join(list(map(str,ans[i]))))
            else:
                ans[i] = [ans[i][-1]]+ans[i][0:-1]
                print(' '.join(list(map(str,ans[i]))))
                
        
        
       

