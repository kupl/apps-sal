# cook your dish here
x=[chr(i) for i in range(48,57)]
y=input()
c=''
s=''
i=0
p=0
while i<len(y):
    if y[i] in x:
        p=int(y[i])
        i=i+1
        if y[i]=='+':
            i+=1
            while y[i]!='-':
                c=c+y[i]
                i=i+1
        i+=1
        s=s+c*p
        c=''
        #print(s)
    else:
        s=s+y[i]
        #print(s)
        i=i+1
if s==s[::-1]:
    print("Return")
else:
    print("Continue")
