s=list(input())
st=[]
cnt=0
for i in s:
    if len(st)==0 or st[-1]!=i:
        st.append(i)
    elif st[-1]==i:
        st.pop()
        cnt+=1
if cnt&1:print('Yes')
else:print('No')
