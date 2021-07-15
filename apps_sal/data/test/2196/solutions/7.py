n=int(input())
a=list(map(int,input().split()))
st=set()
for e in a :
    while(e in st):
        st.remove(e)
        e+=1
    st.add(e)
print(max(st)-len(st)+1)

