# cook your dish here
a,b,c=map(int,input().split())
c=c-a
if((c//b)%2==0):
    print('Lucky Chef')
else:
    print('Unlucky Chef')
