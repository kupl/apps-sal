n = int(input())
a = list(input().split())
st = []
for i in a:
    tmp = set()
    for j in i:
        tmp.add(j)
    if tmp not in st:
        st.append(tmp)

print(len(st))
