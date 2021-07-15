n,m=map(int, input().split())
x_list=[int(i) for i in input().split()]

x_list.sort()

differ_list=[]

for i in range(m-1):
    differ_list.append(x_list[i+1]-x_list[i])
    
if n>=m:
    ans=0
else:
    differ_list.sort(reverse=True)
    ans=sum(differ_list[n-1:])
    
print(ans)
