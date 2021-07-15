from sys import stdin
def main():
    f=open("input.txt")
    fin=open("output.txt","w")
    horas=[int(x)for x in f.readline().strip().split()]
    luz=[int(x)for x in f.readline().strip().split()]
    posiciones=list(range(1,len(luz)+1))   
    s=list(zip(luz,posiciones))
    x=list()
    s.sort()
    z=list()
    eliminado=horas[0]-horas[1]
    for i in range(eliminado,len(s)):
        x.append(s[i])
    for u in range (len(x)):
        z.append(x[u][1])
    z.sort()    
    fin.write(str(x[0][0]) + "\n")
    for c in range(len(z)):
        fin.write( str(z[c]) + " ")

    fin.close()
    f.close()
main()

