n = list(map(int,input().split()))
a = sum(n)
if a%5 == 0 and a!=0:
    print(a//5)
else :
    print('-1')
