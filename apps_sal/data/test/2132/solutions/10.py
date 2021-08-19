(n, d) = (int(input()), [])
for i in range(n):
    d.append(tuple(map(int, input().split())))
(st, c) = ([], 0)
(ans, v) = (0, 0)
for i in d:
    if i[0] == 1:
        v = i[1]
        while len(st) != 0 and st[-1] < v:
            ans += 1
            st.pop()
    elif i[0] == 2:
        ans += c
        c = 0
    elif i[0] == 3:
        if v > i[1]:
            ans += 1
        else:
            st.append(i[1])
    elif i[0] == 4:
        c = 0
    elif i[0] == 5:
        st.clear()
    elif i[0] == 6:
        c += 1
print(ans)
