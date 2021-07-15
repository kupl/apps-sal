# cook your dish here
try:
    j,s,m=map(int,input().split())
    m=m-j
    b=m//s
    if (b%2==0):
        print('Lucky Chef')
    else:
        print('Unlucky Chef')
except:
    pass
