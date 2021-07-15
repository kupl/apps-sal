n = int(input())
a = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
b = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
c = ['thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
if n==0:
    print('zero')
    quit()
if n<13:
    print(a[n-1])
    quit()
if n>=13 and n<20:
    print(c[n-13])
    quit()
if n%10==0:
    print(b[n//10-2])
    quit()
else:
    print(b[divmod(n,10)[0]-2]+'-'+a[divmod(n,10)[1]-1])
    quit()
