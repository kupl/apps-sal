A,B=list(map(int,(input().split())))
count=0

for C in range(1,4):
    if A*B*C%2==1:
        count=count+1

if count>=1:
    print('Yes')

elif count==0:
    print('No')

