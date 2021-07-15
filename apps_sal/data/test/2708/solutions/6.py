# cook your dish
def solve():


    n,k=map(int,input().split())
    for i in range(k):
        if int(str(n)[-1])>0 :
            n=n-1
        elif int(str(n)[-1])==0 :
            n=n//10
            
    print(n)
t = 1
for __ in range(t):
    solve()
