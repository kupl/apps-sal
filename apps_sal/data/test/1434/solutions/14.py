n, st, xors, sumst, buf = int(input()), [], [], 0, []

for i in range(n):
    s=input().split()
    st.append(int(s[0])); xors.append(int(s[1])); sumst+=st[i]
    if st[i]==1:
        buf.append(i)

if sumst % 2 != 0:
    print("0"); return

print(sumst // 2 )

while buf:
    v=buf.pop()
    if st[v]==1:
        print(str(v)+" "+str(xors[v]))
        xors[xors[v]]^=v; st[xors[v]]-=1
        if st[xors[v]]==1:
            buf.append(xors[v])

