st=[]
s=input()
cn=0

for i in s:
    st.append(i)
    while len(st)>=2 and st[-2]==st[-1]:
        st.pop()
        st.pop()
        cn+=1

print("Yes" if cn%2==1 else "No")
