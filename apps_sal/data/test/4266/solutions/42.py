k,x=map(int, input().split())
a_list=[]

for i in range(2*k-1):
    a_list.append(str(x-k+1+i))
    
print(" ".join(a_list))
