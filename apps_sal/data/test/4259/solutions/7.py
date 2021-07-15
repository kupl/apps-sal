def mult(x,d):
    return x//d


K=int(input())
A,B=map(int,input().split())

if mult(B,K)-mult(A-1,K)>0:
    print('OK')
else:
    print('NG')
