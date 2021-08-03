s = input()
st = []
for e in s:
    if e == 'B':
        if len(st) != 0:
            st.pop()
    else:
        st.append(int(e))
print((''.join(map(str, st))))
