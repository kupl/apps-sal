# cook your dish here
for _ in range(1):
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    if x>y:
        print(n)
    else:
        c=0
        for val in a:
            if val <= x:
               c+=1 
        print((c+1)//2)
