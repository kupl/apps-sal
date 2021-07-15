# cook your dish here
jc,sc,money=map(int,input().split())
money-=jc 
if (money//sc)%2==0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')

