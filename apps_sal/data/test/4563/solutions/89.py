n=int(input())
ans_t=1
ans_a=1
for i in range(n):
    t,a=map(int,input().split())
    if t==1:
        k1=ans_t
    else:
    	k1=(ans_t-1)//t+1
    if a==1:
        k2=ans_a
    else:
    	k2=(ans_a-1)//a+1
    k=max(k1,k2)
    ans_t=k*t
    ans_a=k*a
print(ans_t+ans_a)
