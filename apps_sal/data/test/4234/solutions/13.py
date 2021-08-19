# codeforces1165C_live
def gi(): return list(map(int, input().strip().split()))


n, = gi()
s = list(input())
st = []
for e in s:
    if st and st[-1] == e and len(st) % 2:
        st.pop()
        st.append(e)
    else:
        st.append(e)
if len(st) % 2:
    st.pop()
print(n - len(st))
print("".join(st))
