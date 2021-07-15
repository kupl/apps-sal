inStr=input()
n=int(inStr.split()[0])
x0=int(inStr.split()[1])
y0=int(inStr.split()[2])

s=set()
inf=10e18
for i in range(n):
    inStr=input()
    x=int(inStr.split()[0])
    y=int(inStr.split()[1])
    #k and b will be in a denominator form, (k,b) is the line equation
    if (x==x0):
        #k=(y-y0, 0)
        k=inf
        b=x0
    else:
        k = ((y-y0), (x-x0))
        k= k[0]/k[1]
        b = y0 - k*x0
        #b = (y, k[0], k[1])
    s.add((k, b))

#print(s)
print(len(s))
