n=int(input())
a=[0]
for i in range(n):
    a.append(list(input()))
x=int(input())
b=list(map(int,input().split()))
if x==2:
    print(2)
    print(*b)
    return
st=[b[0]]
st1=[b[0]]
k=b[1]
for i in range(1,n+1):
    a[i][i-1]='1'
    
# print(a)
pr=[]
pr.append(b[0])
# print(,end=" ")
for j in range(2,x):
    for l in st1:
        # print(st,st1,k,b[j])
        if a[l][b[j]-1]=='1':
            st.append(k)
            st=[k]
            st1=[k]
            # print(k,end=" ")
            pr.append(k)
            k=b[j]
            
            break
    else:
        st1.append(b[j])
        k=b[j]
pr.append(b[-1])        
# print(b[-1])    
print(len(pr))
print(*pr)
        
        
        
    

