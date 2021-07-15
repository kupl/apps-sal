n = int ( input ())
a = [ 0 ] + list (map(int,input().split()))
z=[]
while n != 0:
    z +=[n]
    n = a [ n -1 ]
z.reverse()
for i in z:
    print(i,end=" ")


