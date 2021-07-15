a,b=map(int,input().split(':'))
c,d=map(int,input().split(':'))
m=(a*60+b+c*60+d)//2
print(('0'+str(m//60))[-2:],('0'+str(m%60))[-2:],sep=':')

