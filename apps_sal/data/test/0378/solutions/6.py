k,r=list(map(int,input().split()))
for i in range(1,11):
    if (k*i)%10==r or (k*i)%10==0:
        print(i)
        break

