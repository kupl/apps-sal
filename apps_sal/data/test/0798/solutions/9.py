a,b,c = map(int, input().split())
x = ((a+b)-c)//2
y = ((b+c)-a)//2
z = ((a+c)-b)//2
if (x + z) == a and (x+y) == b and (y + z) == c and x > -1 and y > -1 and z > -1:
   print(x,y,z, sep = ' ')
else:
    print("Impossible")

