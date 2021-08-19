n = int(input())
st = set()
for e in map(int, input().split()):
   # print(st,'beg')
    while(e in st):
        st.remove(e)
        e += 1
    st.add(e)
    # print(st)
print(max(st) - len(st) + 1)
# print(max(st))
