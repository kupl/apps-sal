s = input()
ans = ['0' for i in range(len(s))]
st = []
for i in range(len(s)):
    if s[i] == '0':
        if len(st):
            ans[st.pop()] = '1'
    else:
        st.append(i)
print(''.join(ans))
