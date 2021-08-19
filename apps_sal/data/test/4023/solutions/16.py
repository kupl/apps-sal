n = int(input())
l = [int(x) for x in input().split()]
st = []
for i in l:
    d = i
    if len(st) and st[-1] == d:
        st.pop()
    elif len(st) == 0 or st[-1] > d:
        st.append(d)
    else:
        print('NO')
        break
else:
    if len(st) == 0 or (len(st) == 1 and st[-1] == max(l)):
        print('YES')
    else:
        print('NO')
