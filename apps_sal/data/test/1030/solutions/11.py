from sys import stdin
def main():
    h=[]
    c=[]
    j=[]
    x=stdin.readline().split()
    i=0
    while int(x[1])+1+i<=int(x[0]) and (i<int(x[2])):
        h.append(int(x[1])+i+1)
        i=i+1
    i=0
    while int(x[1])-1-i>=1 and (i<int(x[2])):
        c.append(int(x[1])-i-1)
        c.sort()
        i=i+1
    if len(c)>=1:
        if c[0]>1:
            c.insert(0,("<<"))
    if len(h)>=1:
        if int(x[0])>(h[len(h)-1]):
            h.append(str(">>"))
    g=str('('+x[1]+')').split()
    j=c+g+h
    for i in range (len(j)):
        j[i]=str(j[i])
    d=" ".join(j)
    print (d)           
        
main()
