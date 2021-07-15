for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    same=False
    possible=True
    l=[]
    for i in range(n):
        if s1[i]!=s2[i]:
            l.append([s1[i],s2[i]])
        else:
            same=True
   # print(l)
    if len(l)==0 and same:
        print("Yes")
    elif len(l)==2 and l[0][0]==l[1][0] and l[0][1]==l[1][1]:
        print("Yes")
    else:
        print("No")
