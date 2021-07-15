n, a, b = map(int,input().split())
M = 10**9+7
Answer = pow(2,n,M)-1
factorial=1
for i in range(1,a+1):
    factorial = (factorial*(n+1-i)*pow(i,M-2,M))%M
Answer -= factorial%M
factorial =1
for j in range(1,b+1):
    factorial = (factorial*(n+1-j)*pow(j,M-2,M))%M
Answer -= factorial%M
Answer = Answer%M
print(Answer)
