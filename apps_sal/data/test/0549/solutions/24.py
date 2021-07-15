def problem(n):
    b=[]
    b=[x for x in range(1, n+1) if n % x == 0]
    return b[len(b)//2]
    
a=int(input())
c=problem(a)
print(a//c,c)
