s = input()
d = ['a', 'e', 'i', 'o', 'u']
st = []
for i in range(len(s)):
    if s[i] in d:
        st = []
        print(s[i], end='')
        continue
    st.append(s[i])
    if st == [s[i], s[i], s[i]]:
        st = st[1:]
        print(s[i], end='')
    elif len(st) == 3:
        st = [s[i]]
        print(' ' + s[i], end='')
    else:
        print(s[i], end='')
