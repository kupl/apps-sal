b,a=list(map(int,input().split()))
delit=[]
st=[]
i=2
uk=-1
while i*i<=a:
    if a%i==0:
        delit.append(i)
        uk+=1
        st.append(0)
        while a%i==0:
            a//=i
            st[uk]+=1
    i+=1
if a>1:
    delit.append(a)
    st.append(1)
coun=0
colvo=[0]*len(st)
cop=b
for i in range(len(delit)):
    while cop>=delit[i]:
        colvo[i]+=cop//delit[i]
        cop//=delit[i]
    cop=b
coun=colvo[i]//st[i]
for i in range (len(st)):
    if colvo[i]//st[i]<coun:
        coun=colvo[i]//st[i]
print(coun)

