ans = 0
n = 0
n = int(input(""))
l = input("")
st = []
for x in l.split(" "):
    st.append(int(x))
st.sort()
i = n - 1
while i >= 3:
    if st[i] > st[i - 1] + 1:
        i = i - 1
        continue
    l = st[i - 1]
    i = i - 2
    while i > 0 and st[i] > st[i - 1] + 1:
        i = i - 1
    if i == 0:
        break
    b = st[i - 1]
    ans = ans + l * b
    i = i - 2
print(ans)
