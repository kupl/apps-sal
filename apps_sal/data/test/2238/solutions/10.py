__author__ = 'gen'
n=int(input())
for i in range(1,n,2):
    z=int((n-i)/2)
    print('*'*z+'D'*i+'*'*z)
print('D'*n)
for i in range(n-2,0,-2):
    z=int((n-i)/2)
    print('*'*z+'D'*i+'*'*z)
