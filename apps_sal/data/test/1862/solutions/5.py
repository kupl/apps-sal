n = int(input())
st = set()
ans = 0
for i in map(int, input().split()):
    if i not in st:
        st.add(i)
        ans = max(ans, len(st))
    else:
        st.remove(i)
print(ans)
