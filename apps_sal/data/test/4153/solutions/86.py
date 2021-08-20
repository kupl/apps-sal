s = input()
st = []
ans = 0
for e in s:
    if len(st) == 0:
        st.append(e)
    elif st[-1] != e:
        st.pop()
        ans += 2
    else:
        st.append(e)
print(ans)
