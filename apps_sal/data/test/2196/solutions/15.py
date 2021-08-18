n = int(input())
st = set()
for e in map(int, input().split()):
    while(e in st):
        st.remove(e)
        e += 1
    st.add(e)
print(max(st) - len(st) + 1)
