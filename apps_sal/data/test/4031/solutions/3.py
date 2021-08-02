n = int(input())
st = []
for i in range(n):
    st.append(input())

for i in range(n - 1):
    for j in range(i, n):
        if (not(st[i] in st[j])) and (not(st[j] in st[i])):
            print("NO")
            quit()
        if (st[j] in st[i]):
            wk1 = st[i]
            st[i] = st[j]
            st[j] = wk1

print("YES")
for i in st:
    print(i)
