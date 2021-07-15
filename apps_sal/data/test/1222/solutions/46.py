from itertools import accumulate
K=int(input())
a0,a1,a2,a3,a4,a5,a6,a7,a8,a9=1,1,1,1,1,1,1,1,1,1
Alist=[[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]]
sumation=9
sumations=[0,9]
digit=0
ans=[]
while sumation<K:
    an0=a0+a1
    an1=a0+a1+a2
    an2=a1+a2+a3
    an3=a2+a3+a4
    an4=a3+a4+a5
    an5=a4+a5+a6
    an6=a5+a6+a7
    an7=a6+a7+a8
    an8=a7+a8+a9
    an9=a8+a9
    a0,a1,a2,a3,a4,a5,a6,a7,a8,a9=an0,an1,an2,an3,an4,an5,an6,an7,an8,an9
    sumation+=a1+a2+a3+a4+a5+a6+a7+a8+a9
    digit+=1
    Alist.append([a0,a1,a2,a3,a4,a5,a6,a7,a8,a9])
    sumations.append(sumation)
K-=sumations[-2]
for num in range(9):
    l=list(accumulate(Alist[-1]))
    if l[num]-l[0]<K<=l[num+1]-l[0]:
        K-=l[num]-l[0]
        break
ans.append(str(num+1))
for i in range(digit):
    for n in range(max(0,num),min(num+3,10)):
        K-=Alist[-i-2][n]
        if K<=0:
            K+=Alist[-i-2][n]
            break
    num=n-1
    ans.append(str(num+1))
print(int(''.join(ans)))
