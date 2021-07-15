w,a,b=map(int,input().split())
A=[i for i in range(a,a+w+1)]
B=[i for i in range(b,b+w+1)]
if a in B or b in A:
    print(0)
else:
    print(min(abs(a+w-b),abs(b+w-a)))
