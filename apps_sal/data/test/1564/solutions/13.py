def countchar(s1,s2):
    vala = s1.count("a") + s2.count("a")
    valb = s2.count("b") + s2.count("b")
    if(vala%2 == 0 and valb%2 == 0):
        return True
    else:
        return False

def calcarr(s1,s2):
    a2b,b2a=[],[]
    sol=[]
    for i in range(len(s1)):
        if(s1[i]=="a" and s2[i]=="b"):
            a2b.append(i)
        elif(s1[i]=="b" and s2[i]=="a"):
            b2a.append(i)
    
    k=0
    if(len(a2b)%2 ==0 and len(b2a)%2==0):

        for i in range(1,len(a2b),2):
            sol.append([a2b[i-1]+1,a2b[i]+1])
            k+=1

        for i in range(1,len(b2a),2):
            sol.append([b2a[i-1]+1,b2a[i]+1])
            k+=1

    else:

        for i in range(1,len(a2b),2):
            sol.append([a2b[i-1]+1,a2b[i]+1])
            k+=1

        for i in range(1,len(b2a),2):
            sol.append([b2a[i-1]+1,b2a[i]+1])
            k+=1

        sol.append([a2b[-1]+1,a2b[-1]+1])
        sol.append([a2b[-1]+1,b2a[-1]+1])
        k+=2

    print(k)
    for i in sol:
        print(i[0],i[1])


def main():

    n= int(input())
    s1 = input()
    s2 = input()

    if(countchar(s1,s2)):
        calcarr(s1,s2)
    else:
        print("-1")


def __starting_point():
    main()
__starting_point()
