p = 998244353
A,B,C = map(int,input().split())
x = ((A*(A+1))//2)%p
x = (x*(B*(B+1))//2)%p
x = (x*(C*(C+1))//2)%p
print(x)
