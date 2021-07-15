s = input()
cnt = 0
st = []
for elem in s:
    if elem in '([{<':
        st.append(elem)
    else:
        if len(st) == 0:
            print('Impossible')
            break
        elem2 = st.pop()
        if elem2 + elem not in '()[]{}<>':
            cnt += 1
else:
    if len(st) == 0:
        print(cnt)
    else:
        print('Impossible')
