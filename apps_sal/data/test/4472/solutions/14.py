n=int(input())
s=input()
s1=input()
ans=0
for i in range(n//2):
    a=s[i]
    b=s[n-1-i]
    x=s1[i]
    y=s1[n-1-i]
    st=set()
    st1=set()
    st2=set()
    st.add(a)
    st.add(b)
    st1.add(x)
    st1.add(y)
    st2.add(a)
    st2.add(b)
    st2.add(x)
    st2.add(y)
    if len(st2)==4:
        ans+=2
    elif len(st2)==3:
        if len(st)==1 and len(st1)==2:
            ans+=2
        if len(st1)==1 and len(st)==2:
            ans+=1
        if len(st1)==2 and len(st)==2:
            ans+=1
        
    elif len(st2)==2:
        if (len(st)==2 or len(st1)==2 ) and (len(st)!=len(st1)):
            ans+=1
if n%2!=0:
    if s[n//2]!=s1[n//2]:
        ans+=1
print(ans)

