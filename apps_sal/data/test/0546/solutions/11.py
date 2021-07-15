l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s1=input().strip()
s1=list(s1)
s2=[]
for i in l:
    if i not in s1:
        s2.append(i)
pattern=input().strip()
pattern=list(pattern)
if ("*" not in pattern):
    length_main=len(pattern)
    n=int(input().strip())
    for i in range(n):
        f=0
        string=input().strip()
        length=len(string)
        if (length_main==length):
            for j in range(length_main):
                if (string[j]!=pattern[j]):
                    if (pattern[j]!="?"):
                        print ('NO')
                        f=1
                        break
                    else:
                        if (string[j] not in s1):
                            print ('NO')
                            f=1
                            break
            if (f==0):
                print ("YES")
        else:
            print ('NO')
else:
    ind=pattern.index("*")
    length_main=len(pattern)
    n=int(input().strip())
    for i in range(n):
        string=input().strip()
        length=len(string)
        if (length<length_main-1):
            print ('NO')
        else:
            f=0
            for j in range(ind):
                if (string[j]!=pattern[j]):
                    if (pattern[j]!="?"):
                        print ('NO')
                        f=1
                        break
                    else:
                        if (string[j] not in s1):
                            print ('NO')
                            f=1
                            break
            if (f!=1):
                q=length_main-length
                for j in range(length_main-1,ind,-1):
                    if (string[j-q]!=pattern[j]):
                        if (pattern[j]!="?"):
                            print ('NO')
                            f=1
                            break
                        else:
                            if (string[j-q] not in s1):
                                print ('NO')
                                f=1
                                break
                if (f!=1):
                    save= ind+1-q
                    string=list(string)
                    x=string[ind:save]
                    for j in x:
                        if (j not in s2):
                            print ('NO')
                            f=1
                            break
                    if (f==0):
                        print ('YES')
