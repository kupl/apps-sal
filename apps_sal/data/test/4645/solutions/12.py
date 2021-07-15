t = int(input())
for i in range(t):
    n=int(input())
    if n==2:
        print(-1)
        continue
    if n==3:
        print(-1)
        continue
    if n==4:
        print(3,1,4,2)
        continue
    if n==5:
        print(1,3,5,2,4)
        continue
    if n%2==0:
        for i in range(n//2):
            print(i*2+1,end=' ')
        print(n - 4, n, n - 2, end=' ')
        for i in range(n//2-3):
            print(n-6-2*i, end=' ')
        print()
    if n%2==1:
        for i in range(n//2+1):
            print(i*2+1,end=' ')
        print(n-3, n-1, end=' ')
        for i in range(n//2-2):
            print(n-5-2*i, end=' ')
        print()
        
    
        
