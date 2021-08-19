def __starting_point():
    (n, k) = list(map(int, input().split()))
    aa = list(input())
    st = {''.join(aa)}
    arr = [aa]
    w = 0
    c = 0
    cst = 0
    while len(arr) < k and w < len(arr):
        wrd = arr[w][:c] + arr[w][c + 1:]
        wrds = ''.join(wrd)
        if wrds not in st:
            st.add(wrds)
            arr.append(wrd)
            cst += n - len(wrd)
        c += 1
        if c >= len(arr[w]):
            c = 0
            w += 1
    if len(arr) < k:
        print(-1)
    else:
        print(cst)


__starting_point()
