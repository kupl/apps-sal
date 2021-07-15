I=lambda:list(map(int,input().split()))
R=list(range(999))
q,w,e=I()
r,t,y=I()
a,b,c=I()
print(min(i*b+j*c+max(0,(r//(w+i-y)+bool(r%(w+i-y)))*(t-e-j)-q+1)*a for i in R for j in R if w+i>y))

