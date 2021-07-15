T = int(input())
ans = 0
top = -1
stack = []
times = 1
j = 0
bj = 0
while T>0:
    T = T - 1
    s = input().strip().split()
    if len(s)==1:
        if s[0]=="add":
            ans+=times
        else:
            if j==0:
                times//=stack[top]
                top-=1
            else:
                j-=1
    else:
        x=int(s[1])
        
        if times<=4294967295:
            times*=x
            top+=1
            if top>=len(stack):
                stack.append(x)
            else:
                stack[top]=x
        else:
            j+=1
        
    if ans>4294967295:
        bj=1
        break
if bj==0:
    print(ans)
else:
    print("OVERFLOW!!!")
