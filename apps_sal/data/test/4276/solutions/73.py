N,T=list(map(int, input().split()))
c_list=[]

for i in range(N):
    c,t=list(map(int, input().split()))
    if t<=T:
        c_list.append(c)

if c_list==[]:
    print("TLE")
    
else:
    print((min(c_list)))

