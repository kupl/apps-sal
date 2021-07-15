n=int(input())
a=int(input())
b=int(input())
c=int(input())
litr =0
cen = b-c
if n>=a or n>=b:
    if cen < a and n>=c:
        litr = (n-c)//(b-c)
        n-=litr*(b-c)
litr += n//a
print(litr)

