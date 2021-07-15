n=int(input())
a=list(map(int,input().split()))
m=max(a)
b=[]
for i in a:
    b.append(m-i)
st=[b[0]]
for i in range(1,n):
    if st and st[-1]==b[i]:
        st.pop()
    elif st and b[i]>st[-1]:
        st.append(b[i])
    elif st:
        print('NO');return
    else:
        st.append(b[i])
if len(st)==0 or st[-1]==0:
    print('YES')
else:
    print('NO')
