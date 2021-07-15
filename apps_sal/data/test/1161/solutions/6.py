s2=input()
dic={'{':1,'}':-1,'<':2,'>':-2,'[':3,']':-3,'(':4,')':-4}
stack=[]
count=0
n=0
for x in s2:
    if dic[x]<0:
        if n==0:
            print("Impossible")
            quit()
        if dic[stack[n-1]]+dic[x]!=0:
            count+=1
        stack.pop()
        n=n-1
    else:
        stack.append(x)
        n=n+1
if n!=0:
    print("Impossible")
else:
    print(count)

