for _ in range(int(input())):
    data = list(map(int,list(input())))
    fl = False
    data.append("&")
    l = 0
    st = []
    for i in range(len(data)):
        if fl and data[i] == 1:
            l+=1
            continue
        if fl and data[i]!=1:
            st.append(l)
            l = 0
            fl = False
            continue
        if not fl and data[i] == 1:
            l = 1
            fl = True
    st.sort(reverse=True)
    c1 = 0
    for i in range(0,len(st),2):
        c1+=st[i]
    print(c1)
