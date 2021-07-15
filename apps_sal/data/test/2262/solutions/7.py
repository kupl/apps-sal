n=int(input())
se=input().split()
st=set()
for x in range(n):
    s=se[x]
    s=set(s)
    st.add(tuple(sorted(list(s))))
print(len(st))
