n=int(input())
l=input()
r=input()

l2=[[l[i],i+1] for i in range(n)]
r2=[[r[i],i+1] for i in range(n)]

l2.sort(reverse=True)
r2.sort(reverse=True)

l_i=0
r_i=0

ANS=[]

check_l=[0]*n
check_r=[0]*n
while l_i<n and r_i<n and l2[l_i][0]!="?" and r2[r_i][0]!="?":
    if l2[l_i][0]==r2[r_i][0]:
        ANS.append([l2[l_i][1],r2[r_i][1]])
        check_l[l_i]=1
        check_r[r_i]=1
        l_i+=1
        r_i+=1
    elif l2[l_i][0]>r2[r_i][0]:
        l_i+=1
    elif l2[l_i][0]<r2[r_i][0]:
        r_i+=1

j=0    
for i in range(n-1,-1,-1):
    if l2[i][0]!="?":
        break
    if check_l[i]==1:
        continue
    while check_r[j]==1:
        j+=1
    ANS.append([l2[i][1],r2[j][1]])
    check_l[i]=1
    check_r[j]=1

j=0    
for i in range(n-1,-1,-1):
    if r2[i][0]!="?":
        break
    if check_r[i]==1:
        continue
    while check_l[j]==1:
        j+=1
    ANS.append([l2[j][1],r2[i][1]])
    check_l[j]=1
    check_r[i]=1

print(len(ANS))
for ans in ANS:
    print(*ans)
    

