n=int(input())
a=list(map(int,input().split()))
st=[a[0]]
for i in range(1,n):
    if len(st)>0 and st[-1]%2==a[i]%2:
        st.pop()
    else:
        st.append(a[i])
if len(st)<=1:
    print("YES")
else:
    print("NO")

