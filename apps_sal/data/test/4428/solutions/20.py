n=int(input())
a=list(map(int,input().split()))
suma=i=0
flag=0
sum1=0
sum3=0
j=n-1
idxs=i
idxe=j
while(True):
    if((sum1==0 and sum3==0) or (sum1<sum3)):
        sum1+=a[i]
        i+=1
    elif(sum3<sum1):
        sum3+=a[j]
        j-=1
    elif(sum1==sum3):
        suma+=sum1
        flag=1
        sum1=0
        sum3=0
    if(j<i-1):
        break
    

if(flag):
    print(suma)
else:
    print(0)

