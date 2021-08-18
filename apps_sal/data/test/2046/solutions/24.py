n = int(input())
lst = list(map(int, input().split()))
st = set()
idx = n
for i in range(len(lst)):
    x = lst[i]
    if x == idx:
        pt = [x]
        idx -= 1
        while idx in st:
            pt.append(idx)
            idx -= 1
        print(' '.join([str(i) for i in pt]))
    else:
        print()
        st.add(x)
