def main():
    f=open("input.txt","r")
    inp= f.readline().split()
    inp=[int(i) for i in inp];
    num= f.readline().split()
    num=[int(i) for i in num];
    num2=[];
    for i in range(len(num)):
        num2.append(num[i]);
    num2.sort()
    num2.reverse()
    x=int(inp.pop())
    y = num2[x-1];
    p=[];
    cont=0;
    for i in range(len(num)):
        if(num[i]>=y and cont<x):
            p.append(i+1);
            cont+=1
    g=open("output.txt","w") 
    g.write(str(y))
    g.write("\n")
    g.write(' '.join(str(e) for e in p));
    g.close()
    f.close()
main()

