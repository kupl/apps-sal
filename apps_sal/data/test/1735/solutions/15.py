s = input()
st = ['']
k = 0
for c in s:
    if c == st[-1]:
        k += 1
        st.pop()
    else:
        st.append(c)
print('Yes' if k % 2 == 1 else 'No')
