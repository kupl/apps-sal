s = input().strip()
st = ['!']
for si in s:
    if st[-1]==si:
        st.pop()
    else:
        st.append(si)
print('Yes' if len(st)==1 else 'No')
