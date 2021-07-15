a=input().split(' ')
n=int(a[0])
t=int(a[1])
a=input().split(' ')
a=[int(i) for i in a]
for i in range(n):
    if t<=0:
        print(i)
        break
    t=t-(86400-a[i])
else:
    print(n)
        

