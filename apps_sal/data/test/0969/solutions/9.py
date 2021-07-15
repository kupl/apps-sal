s1 = input()
s= input()+'.'
s2=s1[::-1]
l=len(s)
ll=len(s1)
a=''
lis=[]
for i in range(l):
    v=a+s[i]
    if v in s1 or v in s2:
         a=a+s[i]
    else:
        if a in s1:
            k=s1.index(a)+1
            lis.append([k,k+len(a)-1])
#            print(s1.index(a),a)
        elif a in s2:
            k=s2.index(a)
            lis.append([ll-k,ll-k-(len(a)-1)])
#            print(k)
        else:
            print(-1)
            return
        a=s[i]
print(len(lis))                    
for i in lis:
    print(*i)

