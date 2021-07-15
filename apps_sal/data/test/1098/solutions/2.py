import sys
n=int(input())
if n==1:
    print('23:59')
    return
a=[]
for i in range(n):
    k,b=map(int,input().split(':'))
    a+=[k*60+b]

a=sorted(a)

mn=0
for i in range(1,n):
    mn=max(mn,a[i]-a[i-1])
mn=max(mn,24*60-a[n-1]+a[0])
mn-=1
s=''
if(mn//60<10): s+='0'
s+=str(mn//60)
s+=':'
if(mn%60<10): s+='0'
s+=str(mn%60)
print(s)
