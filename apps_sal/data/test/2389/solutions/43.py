n,a,b,c=list(map(int,input().split()))
if a+b+c==0:
    print("No")
elif a+b+c==1:
    d=[]
    for i in range(n):
        s=input()
        if s=="AB":
            if a+b==0:
                print("No")
                return
            else:
                if a==0:
                    d.append("A")
                else:
                    d.append("B")
                a,b=b,a
        if s=="BC":
            if c+b==0:
                print("No")
                return
            else:
                if b==0:
                    d.append("B")
                else:
                    d.append("C")
                c,b=b,c
        if s=="AC":
            if a+c==0:
                print("No")
                return
            else:
                if a==0:
                    d.append("A")
                else:
                    d.append("C")
                a,c=c,a 
    print("Yes")
    for i in d:
        print(i)
else:
    d=[]
    s=[input()for i in range(n)]+["AB"]
    for i in range(n):
        if s[i]=="AB":
            if a+b==0:
                print("No")
                return
            if a+b+c==2 and a==1 and b==1 and s[i+1]!=s[i]:
                if s[i+1]=="AC":
                    d.append("A")
                    a+=1
                    b-=1
                else:
                    d.append("B")
                    b+=1
                    a-=1
            elif a<b:
                d.append("A")
                a+=1
                b-=1
            else:
                d.append("B")
                b+=1
                a-=1
        elif s[i]=="BC":
            if c+b==0:
                print("No")
                return
            if a+b+c==2 and c==1 and b==1 and s[i+1]!=s[i]:
                if s[i+1]=="AB":
                    d.append("B")
                    c-=1
                    b+=1
                else:
                    d.append("C")
                    c+=1
                    b-=1
            elif b<c:
                d.append("B")
                b+=1
                c-=1
            else:
                d.append("C")
                c+=1
                b-=1
        elif s[i]=="AC":
            if c+a==0:
                print("No")
                return
            if a+b+c==2 and c==1and a==1 and s[i+1]!=s[i]:
                if s[i+1]=="AB":
                    d.append("A")
                    a+=1
                    c-=1
                else:
                    d.append("C")
                    c+=1
                    a-=1
            elif a<c:
                d.append("A")
                a+=1
                c-=1
            else:
                d.append("C")
                c+=1
                a-=1
    print("Yes")
    for i in d:
        print(i)

