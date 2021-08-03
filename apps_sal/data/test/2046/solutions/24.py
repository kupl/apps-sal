n = int(input())
lst = list(map(int, input().split()))
# lst = [int(i) for i in list(input()) if i!=' ']
# print(lst)
st = set()
idx = n
for i in range(len(lst)):
    x = lst[i]
    if x == idx:
        pt = [x]
        # print(pt)
        idx -= 1
        while idx in st:
            pt.append(idx)
            idx -= 1
        print(' '.join([str(i) for i in pt]))
    else:
        print()
        st.add(x)
