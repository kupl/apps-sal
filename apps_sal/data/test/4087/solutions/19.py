def summa(x):
    x=str(x)
    otv=0
    for i in x:
        otv+=int(i)
    return otv
n=int(input())
a=n
while summa(a)%4!=0:
    a+=1
print(a)

