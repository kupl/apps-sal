def kkr():
    n, m= [int(i) for i in input().split()]
    a= []
    for i in range(n):
        a.append([i for i in input()])
    ans= 0
    
    for i in range(m):
        for j in range(n-1):
            if a[j][:i+1]> a[j+1][:i+1]:
                for k in range(n):
                    a[k][i]= "z"
                ans+= 1
                break
    
    print(ans)

kkr()
        

