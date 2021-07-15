n=int(input())
if n==1:
    print(1);return
y=n
i=1
while n!=0:
    j=n//2+n%2
    if i*2>y and n==1:
        i=i>>1
        x=y//i
        print(i*x)
    else:
        print((str(i)+' ')*j,end='')
    i=i<<1
    n=n//2
