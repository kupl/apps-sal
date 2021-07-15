n=int(input())
st=[]
ans,now=0,1
for i in range(2*n):
    s=input()
    if s[0]=="a":
        st.append(int(s[4:]))
    else:
        if len(st)==0:
            now+=1
        else:
            if st[-1]==now:
                now+=1
                st.pop()
            else:
                st=[]
                ans+=1
                now+=1
print(ans)

