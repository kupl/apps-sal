count=0;
l,r=input().split();
l=int(l);
r=int(r);
for i in range(31):
    for j in range(20):
        if pow(2,i)*pow(3,j)>=l and pow(2,i)*pow(3,j)<=r :
            count=count+1;
print(count)
