import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''


n=int(input())
ans=0
for i in range(1,n+1):
    ans+=i*(n//i)*(1+n//i)//2
print(ans)
