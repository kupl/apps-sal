R = lambda : map(int, input().split())
a = int(input())
b = int(input())
if (a>b):
    a,b=b,a
m=(a+b)//2
d=lambda x: (x*(x+1))//2
print(d(m-a)+d(b-m))
