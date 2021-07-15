T=int(input())
for _ in range(T):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if min(a,b)*2<=max(a,b):
        print(min(a,b))
    else:
        print(int((a+b)/3))
