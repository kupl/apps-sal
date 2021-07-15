n=int(input())
l=[int(i) for i in input().split()]
slope= (l[n-1]-l[0])/(n-1)
f=0
for j in range(1,n-1):
    if (((l[j]-l[0])/(j))!= slope):
        f=1
        break
if (f==0):
    print ('No')
else:
    flag=0
    for i in range(1,n-1):
        s= (l[i]-l[0])/i
        l1=[]
        for j in range(n):
            l1.append(0)
        l1[0]=1
        l1[i]=1
        l2=[]
        for j in range(i+1,n):
            if ((l[j]-l[0])/j ==s):
                l1[j]=1
        if (l1.count(0)==1):
            print ("Yes")
            flag=1
            break
        else:
            for j in range(n):
                if (l1[j]==0):
                    l2.append([l[j],j])
            length=len(l2)
            s1= (l2[-1][0]-l2[0][0])/(l2[-1][1]-l2[0][1])
            if (s1!=s):
                continue
            else:
                check=0
                for j in range(1,length-1):
                    if ( ((l2[j][0]-l2[0][0])/(l2[j][1]-l2[0][1]))!=s1 ):
                        check=1
                        break
                if (check==1):
                    continue
                else:
                    print ('Yes')
                    flag=1
                    break
    if (flag==0):
        if (n==3):
            print ('Yes')
            flag=1
        else:
            s= (l[-2]-l[1])/ (n-3)
            if (s==slope):
                check=0
                for i in range(2,n-2):
                    if ( ((l[i]-l[1])/(i-1))!=s):
                        check=1
                        break
                if (check==0):
                    print ('Yes')
                    flag=1
        if (flag==0):
            s= (l[-1]-l[1])/(n-2)
            check=0
            for i in range(2,n-1):
                if ( ((l[i]-l[1])/(i-1))!=s ):
                    check=1
                    break
            if (check==0):
                print ('Yes')
            else:
                print ('No')
