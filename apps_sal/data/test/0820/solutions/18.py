n=int(input())
m=int(input())
USB=[]
for i in range(n):
    USB.append(int(input()))
USB.sort()
for i in range(n):
    nu=i
    m-=USB[n-1-i]
    if m<=0:
        break
print(nu+1)
        

